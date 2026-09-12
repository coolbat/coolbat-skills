#!/usr/bin/env python3
"""Export reviewed frames as an RGBA sprite atlas or lossless animated WebP. No artwork generation."""
import argparse
import json
import math
import sys
import tempfile
from pathlib import Path
from PIL import Image, features
from project import alpha_mode, check, digest, load, mode, require, verified_image


def rgba(root, frame):
    with Image.open(verified_image(root, frame)) as im:
        return im.convert('RGBA')


def atlas(root, data, out, columns, padding):
    require(type(columns) is int and 1 <= columns <= 32, 'columns must be 1..32')
    require(type(padding) is int and 0 <= padding <= 64, 'padding must be 0..64')
    require(data.get('sprite'), 'Atlas export requires explicit sprite.clip and sprite.pivot in the plan')
    width, height = data['canvas']['width'], data['canvas']['height']
    cols = min(columns, len(data['frames']))
    rows = math.ceil(len(data['frames']) / cols)
    cell_w, cell_h = width + 2*padding, height + 2*padding
    size = (cell_w*cols, cell_h*rows)
    require(max(size) <= 16384 and size[0]*size[1] <= 64_000_000, 'Atlas exceeds export limits; split clips or use an explicitly resized project')
    sheet = Image.new('RGBA', size, (0,0,0,0))
    entries = []
    elapsed_ticks = 0
    for i, frame in enumerate(data['frames']):
        x,y = (i%cols)*cell_w+padding, (i//cols)*cell_h+padding
        # No mask: copy RGBA samples directly, retaining alpha rather than applying it twice.
        sheet.paste(rgba(root, frame), (x,y))
        entries.append({'id':frame['id'], 'rect':{'x':x,'y':y,'w':width,'h':height},
                        'source_size':[width,height], 'pivot':data['sprite']['pivot'],
                        'start_tick':elapsed_ticks, 'hold_ticks':frame['hold'],
                        'duration_ms':frame['hold']*1000/data['action_fps'],
                        'source_image':frame['image'], 'source_sha256':frame['sha256']})
        elapsed_ticks += frame['hold']
    sheet.save(out)
    with Image.open(out) as decoded:
        require(decoded.size == size and decoded.mode == 'RGBA', 'Atlas verification failed')
    return {'schema':'image-animate-director.atlas.v1', 'clip':data['sprite']['clip'],
            'texture_size':list(size), 'cell_size':[cell_w,cell_h], 'columns':cols, 'padding':padding,
            'pivot_units':'normalized source-canvas coordinates', 'loop':data['loop'],
            'action_fps':data['action_fps'], 'frames':entries,
            'note':'Custom metadata, not a native Godot/Unity/Phaser resource. Frames are untrimmed and unscaled; no automatic recentering or extrusion.'}


def webp(root, data, out):
    Image.init()
    require(features.check('webp') and 'WEBP' in Image.SAVE_ALL, 'Pillow with animated WebP support is required')
    frames, delays = [], []
    ticks = previous = 0
    for frame in data['frames']:
        frames.append(rgba(root, frame))
        ticks += frame['hold']
        end = round(ticks*1000/data['action_fps'])
        delays.append(end-previous)
        previous = end
    loop = 0 if data['loop'] else 1
    frames[0].save(out, format='WEBP', save_all=True, append_images=frames[1:],
                   duration=delays, loop=loop, lossless=True, quality=100, method=4, exact=True)
    # Encoders can combine repeated identical frames; validate total time instead of physical frame count.
    total = 0
    with Image.open(out) as decoded:
        require(decoded.size == frames[0].size, 'WebP dimensions differ')
        for i in range(decoded.n_frames):
            decoded.seek(i)
            decoded.load()
            total += decoded.info.get('duration', 0)
        count = decoded.n_frames
    if count > 1:
        require(total == sum(delays), 'WebP duration mismatch')
    return {'duration_ms':sum(delays), 'encoded_frames':count, 'loop_count':loop,
            'timing_verification':'decoded duration checked' if count > 1 else 'static image; encoded playback duration is not retained',
            'source_frames':[{'id':f['id'],'hold':f['hold'],'sha256':f['sha256']} for f in data['frames']],
            'note':'Preserves source alpha; does not remove backgrounds. Delays rounded cumulatively to milliseconds.'}


def export(root, kind, out, columns=4, padding=2):
    data = load(root)
    info = check(root, data)
    require(out.suffix.lower() == ('.png' if kind == 'atlas' else '.webp'), 'Wrong output extension')
    report_path = out.with_suffix(out.suffix+'.json')
    require(not out.exists() and not report_path.exists(), 'Output exists; choose a new version')
    out.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='image-animate-export-', dir=out.parent) as temp:
        candidate = Path(temp)/out.name
        result = atlas(root,data,candidate,columns,padding) if kind == 'atlas' else webp(root,data,candidate)
        require(not out.exists() and not report_path.exists(), 'Output appeared during export')
        candidate.rename(out)
    report = {'file':str(out), 'texture':out.name, 'sha256':digest(out),
              'project_sha256':digest(root/'project.json'), 'mode':mode(data), 'alpha':alpha_mode(data),
              'duration_seconds':info['duration_seconds'], **result}
    report_path.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    return {'file':str(out),'metadata':str(report_path), 'mode':mode(data)}


if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('format',choices=['atlas','webp'])
    parser.add_argument('project',type=Path)
    parser.add_argument('--out',type=Path,required=True)
    parser.add_argument('--columns',type=int,default=4)
    parser.add_argument('--padding',type=int,default=2)
    args=parser.parse_args()
    try:
        print(json.dumps(export(args.project.resolve(),args.format,args.out.resolve(),args.columns,args.padding)))
    except (ValueError,KeyError,TypeError,OSError) as exc:
        print(f'Error: {exc}',file=sys.stderr)
        sys.exit(2)
