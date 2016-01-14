import os
import shutil
import glob

old_dir = '../semantics_pipeline/pipelines_tests/triples'
new_dir = 'ttl'

files = glob.glob(os.path.join(old_dir, '*.ttl'))

for f in files:
    fname = f.split('/')[-1]
    if not os.path.exists(os.path.join(new_dir, fname[0:2])):
        os.mkdir(os.path.join(new_dir, fname[0:2]))
    
    new_f = os.path.join(new_dir, fname[0:2], fname)
    
    shutil.copy(f, new_f)

