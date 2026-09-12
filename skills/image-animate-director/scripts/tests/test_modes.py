"""Mode/export integration fixtures, not evidence of generated animation quality."""
import json
import unittest
from PIL import Image
import test_workflow


class ModeTests(unittest.TestCase):
    setUp = test_workflow.WorkflowTests.setUp
    run_cli = test_workflow.WorkflowTests.run_cli
    init = test_workflow.WorkflowTests.init

    def accepted_transparent(self):
        self.plan.update(mode='animated-sprite', sprite={'clip':'walk','pivot':[0.5,0.875]})
        self.init()
        paths=[]
        for index, frame in enumerate(self.plan['frames']):
            fid=frame['id']
            self.run_cli('project.py','prepare',self.project,'--frame',fid,'--kind','import')
            im=Image.new('RGBA',(64,64),(0,0,0,0))
            # Two differently placed pixels check spatial preservation and soft alpha without image-generation claims.
            im.putpixel((12+index,40),(240,30,70,128))
            im.putpixel((14+index,41),(10,200,80,255))
            path=self.root/(fid+'.png');im.save(path);paths.append(path)
            self.run_cli('project.py','record',self.project,'--frame',fid,'--image',path,'--backend','fixture')
            self.run_cli('project.py','review',self.project,'--frame',fid,'--decision','approve','--notes','Synthetic fixture checked')
        return paths

    def test_atlas_retains_rgba_coordinates_timing_and_pivot(self):
        paths=self.accepted_transparent()
        before=(self.project/'project.json').read_bytes()
        out=self.root/'atlas.png'
        self.run_cli('export_assets.py','atlas',self.project,'--out',out,'--columns','2','--padding','2')
        meta=json.loads(out.with_suffix('.png.json').read_text())
        self.assertEqual(meta['texture_size'],[136,136])
        self.assertEqual([f['hold_ticks'] for f in meta['frames']],[1,2,1])
        self.assertEqual([f['start_tick'] for f in meta['frames']],[0,1,3])
        with Image.open(out) as sheet:
            for frame,source in zip(meta['frames'],paths):
                box=frame['rect'];x,y=box['x'],box['y']
                with Image.open(source) as original:
                    self.assertEqual(sheet.crop((x,y,x+64,y+64)).tobytes(),original.tobytes())
                self.assertEqual(frame['pivot'],[0.5,0.875])
        self.assertEqual(before,(self.project/'project.json').read_bytes())
        self.run_cli('export_assets.py','atlas',self.project,'--out',out,ok=False)

    def test_webp_keeps_alpha_frame_content_and_total_duration(self):
        paths=self.accepted_transparent()
        out=self.root/'motion.webp'
        self.run_cli('export_assets.py','webp',self.project,'--out',out)
        with Image.open(out) as decoded:
            self.assertEqual(decoded.n_frames,3)
            self.assertEqual(decoded.info['loop'],1)
            total=0
            for i in range(3):
                decoded.seek(i);decoded.load()
                total+=decoded.info['duration']
                self.assertEqual(decoded.convert('RGBA').getpixel((12+i,40)),(240,30,70,128))
                self.assertEqual(decoded.convert('RGBA').getpixel((0,0))[3],0)
            self.assertEqual(total,500)

    def test_mode_prompt_and_opaque_rejection(self):
        self.plan.update(mode='animated-sprite', sprite={'clip':'idle','pivot':[0.5,0.9]})
        self.init()
        job=json.loads(self.run_cli('project.py','prepare',self.project,'--frame','f0001').stdout)
        self.assertIn('2D game sprite',job['prompt'])
        self.assertNotIn('stop-motion',job['prompt'])
        self.assertIn('transparent alpha',job['prompt'])
        self.run_cli('project.py','record',self.project,'--frame','f0001','--image',self.root/'master.png',ok=False)

    def test_invalid_mode_and_missing_sprite_rejected(self):
        path=self.root/'bad.json'
        for mode in ['animatedsprite','unknown','animated-sprite']:
            self.plan['mode']=mode;path.write_text(json.dumps(self.plan))
            self.run_cli('project.py','init',self.project,'--plan',path,ok=False)
            self.assertFalse(self.project.exists())

    def test_gif_motion_and_legacy_defaults(self):
        self.plan['mode']='gif-motion'
        self.init()
        job=json.loads(self.run_cli('project.py','prepare',self.project,'--frame','f0001').stdout)
        self.assertIn('animated sticker',job['prompt'])
        self.assertNotIn('stop-motion',job['prompt'])
        path=self.project/'project.json'
        d=json.loads(path.read_text());del d['mode'];path.write_text(json.dumps(d))
        before=path.read_bytes()
        result=json.loads(self.run_cli('project.py','status',self.project).stdout)
        self.assertEqual(result['mode'],'stop-motion')
        self.assertEqual(result['alpha'],'opaque')
        self.assertEqual(before,path.read_bytes())
