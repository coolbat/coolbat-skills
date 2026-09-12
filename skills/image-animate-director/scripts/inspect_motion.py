#!/usr/bin/env python3
"""Read-only adjacent-frame diagnostics and portable timed review; never approves frames."""
import argparse
import base64
import json
import sys
from pathlib import Path
from PIL import Image, ImageChops, ImageStat
from project import check, digest, load, require, timeline, verified_image
from render import rgb_image


def difference(a, b):
    return sum(ImageStat.Stat(ImageChops.difference(a, b)).mean) / (3 * 255)


def regions_difference(a, b, regions):
    result = []
    for region in regions:
        left, top, right, bottom = region['box']
        box = (int(left*a.width), int(top*a.height), max(int(right*a.width), int(left*a.width)+1),
               max(int(bottom*a.height), int(top*a.height)+1))
        score = difference(a.crop(box), b.crop(box))
        threshold = region.get('threshold', 0.03)
        result.append({'id': region['id'], 'mean_absolute_rgb_difference': score,
                       'threshold': threshold, 'flag': score > threshold})
    return result


def analyze(root, data):
    check(root, data)
    frames = data['frames']
    pairs = [(i-1, i) for i in range(1, len(frames))]
    if data['loop']:
        pairs.append((len(frames)-1, 0))
    result = []
    for first, second in pairs:
        a = rgb_image(verified_image(root, frames[first]), data['canvas']['background'])
        b = rgb_image(verified_image(root, frames[second]), data['canvas']['background'])
        result.append({'from': frames[first]['id'], 'to': frames[second]['id'],
                       'whole_frame_difference': difference(a, b),
                       'locked_regions': regions_difference(a, b, data.get('inspection_regions', [])),
                       'loop_seam': second == 0})
    return {'project_sha256': digest(root/'project.json'), 'timeline': timeline(data), 'pairs': result,
            'interpretation': 'Pixel differences are triage signals, not detected camera motion or pose correctness. '
                              'Select regions expected to remain still; inspect flagged pairs visually. '
                              'Unchanged pixels do not prove character identity.',
            'playback_review': 'not performed by this script', 'visual_approval': False}


def payload(root, data, assets):
    result = {'title': data['title'], 'canvas': data['canvas'], 'frames': [],
              'duration': timeline(data)['duration_seconds']}
    end = 0
    for f in data['frames']:
        path = verified_image(root, f)
        sha = f['sha256']
        if sha not in assets:
            with Image.open(path) as im:
                mime = Image.MIME.get(im.format)
            require(mime in ('image/png', 'image/jpeg', 'image/webp', 'image/gif'),
                    'Preview requires PNG/JPEG/WebP/GIF stills')
            assets[sha] = 'data:' + mime + ';base64,' + base64.b64encode(path.read_bytes()).decode('ascii')
        end += f['hold'] / data['action_fps']
        result['frames'].append({'id': f['id'], 'end': end, 'sha': sha, 'goal': f['goal']})
    return result


HTML = '''<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>定格动画对比检查</title><style>
body{margin:0;background:#15191f;color:#eef1f6;font:16px system-ui;padding:24px;max-width:1100px;margin:auto}
h1{font-size:24px} .grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:18px}
figure{margin:0}img{width:100%;display:block;border-radius:16px;object-fit:contain;background:#faf8f5}figcaption{padding:12px 0}
button{padding:10px 18px;border:0;border-radius:8px;margin:6px 4px 6px 0;cursor:pointer}input[type=range]{width:100%}
small,p{color:#bfc8d8;line-height:1.6}output{font-variant-numeric:tabular-nums}label{white-space:nowrap}
</style><h1>定格动画对比检查</h1><p>同步播放，或暂停后逐帧检查。播放速度只影响预览，原片时间不变。</p>
<div class="grid" id="views"></div><div><button id="play" disabled>播放</button><button id="prev" disabled>上一姿态</button><button id="next" disabled>下一姿态</button>
<label>速度 <select id="speed"><option value="0.5">0.5×</option><option value="1" selected>1×</option></select></label>
<label><input type="checkbox" id="repeat">重复预览</label></div><input id="seek" type="range" min="0" step="0.001" value="0" disabled>
<output id="clock">正在加载画面…</output><p id="note">检查眼睛、轮廓、脚部落点和背景。数值差异提示不能代替视觉验收。</p>
<script id="data" type="application/json">__DATA__</script><script>
const data=JSON.parse(document.getElementById('data').textContent), assets=data.assets, shots=data.shots;
const $=id=>document.getElementById(id), duration=Math.max(...shots.map(s=>s.duration));
let t=0,running=false,last=0;
const views=shots.map((s,i)=>{const f=document.createElement('figure'),im=document.createElement('img'),c=document.createElement('figcaption');
im.alt=s.title;im.width=s.canvas.width;im.height=s.canvas.height;f.append(im,c);$('views').append(f);return {im,c};});
function draw(){shots.forEach((s,i)=>{let f=s.frames.find(f=>t<f.end)||s.frames.at(-1);views[i].im.src=assets[f.sha];views[i].c.textContent=s.title+' · '+f.id+' · '+f.goal;});$('seek').value=t;$('clock').textContent=t.toFixed(3)+' / '+duration.toFixed(3)+' 秒';}
function pause(){running=false;$('play').textContent='播放';}
function tick(now){if(running){t+=(now-last)/1000*Number($('speed').value);if(t>=duration){if($('repeat').checked)t%=duration;else{t=duration;pause();}}draw();}last=now;requestAnimationFrame(tick);}
$('play').onclick=()=>{if(running)pause();else{if(t>=duration)t=0;running=true;last=performance.now();$('play').textContent='暂停';}};
$('seek').max=duration;$('seek').oninput=()=>{pause();t=Number($('seek').value);draw();};
const boundaries=[...new Set(shots.flatMap(s=>[0,...s.frames.slice(0,-1).map(f=>f.end)]))].sort((a,b)=>a-b);
function step(dir){pause();t=dir>0?(boundaries.find(x=>x>t+0.00001)??boundaries.at(-1)):([...boundaries].reverse().find(x=>x<t-0.00001)??0);draw();}
$('prev').onclick=()=>step(-1);$('next').onclick=()=>step(1);
Promise.all(Object.values(assets).map(src=>new Promise((resolve,reject)=>{const im=new Image();im.onload=resolve;im.onerror=reject;im.src=src;}))).then(()=>{
['play','prev','next','seek'].forEach(id=>$(id).disabled=false);draw();requestAnimationFrame(tick);
}).catch(()=>{$('clock').textContent='画面加载失败；请检查文件。';});
</script></html>'''


def build(root, out, baseline=None):
    report_path = out.with_suffix('.json')
    require(out.suffix.lower() == '.html', 'Use .html output')
    require(not out.exists() and not report_path.exists(), 'Output exists; choose a new version')
    data = load(root)
    report = {'current': analyze(root, data)}
    assets = {}
    shots = []
    if baseline:
        old = load(baseline)
        report['baseline'] = analyze(baseline, old)
        shots.append(payload(baseline, old, assets))
    shots.append(payload(root, data, assets))
    encoded = json.dumps({'shots': shots, 'assets': assets}, ensure_ascii=False).replace('<', '\\u003c')
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(HTML.replace('__DATA__', encoded), encoding='utf-8')
    report['preview_sha256'] = digest(out)
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    return {'preview': str(out), 'report': str(report_path), 'visual_approval': False}


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('project', type=Path)
    p.add_argument('--out', type=Path, required=True)
    p.add_argument('--baseline', type=Path)
    args = p.parse_args()
    try:
        print(json.dumps(build(args.project.resolve(), args.out.resolve(), args.baseline.resolve() if args.baseline else None)))
    except (ValueError, KeyError, TypeError, OSError) as exc:
        print(f'Error: {exc}', file=sys.stderr)
        sys.exit(2)
