import json
import unittest
import test_workflow


class IterationTests(unittest.TestCase):
    setUp = test_workflow.WorkflowTests.setUp
    run_cli = test_workflow.WorkflowTests.run_cli
    init = test_workflow.WorkflowTests.init
    accept = test_workflow.WorkflowTests.accept
    def test_endpoints_scope_timing_reuse_and_reconsider(self):
        self.plan['references'].append({'id':'raised','role':'Raised endpoint','path':'master.png'})
        self.plan['frames'][0]['reference_ids'] = ['master','raised']
        self.plan['frames'][0]['motion'] = {'phase':'movement','change':['Raise face'], 'lock':['Feet'],
            'between':{'from':'master','to':'raised','progress':0.5}}
        self.init()
        result = self.run_cli('project.py','prepare',self.project,'--frame','f0001','--kind','reuse')
        job = json.loads(result.stdout)
        self.assertIn('50%',job['prompt'])
        self.assertIn('Explicitly lock: Feet',job['prompt'])
        self.assertEqual(len(job['reference_images']),2)
        self.run_cli('project.py','record',self.project,'--frame','f0001','--image',self.root/'master.png')
        self.run_cli('project.py','review',self.project,'--frame','f0001','--decision','reject','--notes','Fixture reject')
        self.run_cli('project.py','reconsider',self.project,'--frame','f0001','--notes','Retained fixture review')
        self.run_cli('project.py','check',self.project,ok=False)
        self.run_cli('project.py','review',self.project,'--frame','f0001','--decision','approve','--notes','Fixture inspected')
        data=json.loads((self.project/'project.json').read_text())
        self.assertEqual(len(data['frames'][0]['attempts']),1)
        self.assertEqual(data['frames'][0]['attempts'][0]['source']['sha256'],data['frames'][0]['sha256'])
        status=json.loads(self.run_cli('project.py','status',self.project).stdout)
        self.assertEqual(status['attempt_kinds']['reuse'],1)
        timeline=json.loads(self.run_cli('project.py','timeline',self.project).stdout)
        self.assertEqual(timeline['timeline'][-1]['end'],0.5)

    def test_missing_endpoint_and_nan_are_rejected(self):
        self.plan['frames'][0]['motion']={'phase':'movement','change':[],'lock':[],
            'between':{'from':'master','to':'missing','progress':0.5}}
        path=self.root/'plan.json'
        path.write_text(json.dumps(self.plan))
        self.run_cli('project.py','init',self.project,'--plan',path,ok=False)
        self.assertFalse(self.project.exists())
        del self.plan['frames'][0]['motion']
        self.plan['inspection_regions']=[{'id':'bad','box':[0,0,float('nan'),1]}]
        path.write_text(json.dumps(self.plan))
        self.run_cli('project.py','init',self.project,'--plan',path,ok=False)

    def test_diagnostics_flag_fixture_change_without_approval_or_mutation(self):
        self.plan['title']='</script><script>alert(1)</script>'
        self.plan['inspection_regions']=[{'id':'locked','box':[0,0,1,1],'threshold':0.01}]
        self.init()
        for fid,color in [('f0001','red'),('f0002','red'),('f0003','blue')]:
            self.accept(fid,color)
        before=(self.project/'project.json').read_bytes()
        out=self.root/'review.html'
        self.run_cli('inspect_motion.py',self.project,'--out',out,'--baseline',self.project)
        report=json.loads(out.with_suffix('.json').read_text())
        pairs=report['current']['pairs']
        self.assertFalse(pairs[0]['locked_regions'][0]['flag'])
        self.assertTrue(pairs[1]['locked_regions'][0]['flag'])
        self.assertFalse(report['current']['visual_approval'])
        self.assertEqual(before,(self.project/'project.json').read_bytes())
        self.assertNotIn(self.plan['title'],out.read_text())
        self.run_cli('inspect_motion.py',self.project,'--out',out,ok=False)
