#!/usr/bin/env python3
from pathlib import Path
import ast,hashlib,importlib.util,json,tempfile,shutil,subprocess,sys
ROOT=Path(__file__).resolve().parents[4];OUT=ROOT/'artifacts/verification';OUT.mkdir(parents=True,exist_ok=True);scratch=Path(tempfile.mkdtemp(prefix='verify-python-examples-'))
proof={'scope':'All9Python sources parse; actual pure sumproduct function and shipped test execute. External/microphone/database/messaging scripts are not executed.','passed':False}
try:
 files=sorted(p for p in ROOT.rglob('*.py') if '.cursor' not in p.parts and 'artifacts' not in p.parts);proof['syntax']=[]
 for p in files:ast.parse(p.read_text());proof['syntax'].append({'file':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
 for p in (ROOT/'pytest').glob('*.py'):shutil.copy2(p,scratch/p.name)
 script='''import importlib.util
spec=importlib.util.spec_from_file_location("sumproduct","sumproduct.py");m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
assert m.sumproduct(3,2)==(5,6)
assert m.sumproduct(0,8)==(8,0)
assert m.sumproduct(-3,2)==(-1,-6)
assert m.sumproduct(1.5,2)==(3.5,3.0)
import sys;sys.modules["sumproduct"]=m
spec=importlib.util.spec_from_file_location("existing_test","test_sumproduct.py");t=importlib.util.module_from_spec(spec);spec.loader.exec_module(t);t.test_sumproduct()
print("sumproduct positive/zero/negative/fractional and existing test passed")
'''
 p=subprocess.run([sys.executable,'-B','-c',script],cwd=scratch,capture_output=True,text=True,timeout=15);proof['arithmetic']={'exit':p.returncode,'stdout':p.stdout,'stderr':p.stderr};assert p.returncode==0,'Arithmetic journey failed'
 proof['unverified']={'weather_requests.py':'requires owner-provided provider key; network not called','weather_latlong_requests.py':'IP geolocation + provider key needed; no location lookup performed','mysql.py':'external database prerequisite; no writes performed','tweet_selenium.py':'external posting/login workflow, not authorized as verification','whatsapp_selenium.py':'external messaging/login workflow, not authorized as verification','speechRecognition.py':'microphone/audio dependency, not available in isolated helper','wordCloud.py':'plotting/window/input-image dependencies not exercised'}
 proof['passed']=True
except Exception as error:proof['failure']=str(error)
finally:
 (OUT/'python-examples.json').write_text(json.dumps(proof,indent=2)+'\n');shutil.rmtree(scratch);assert (OUT/'python-examples.json').exists();print(json.dumps(proof,indent=2))
if not proof['passed']:raise SystemExit(1)
