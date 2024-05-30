import trimesh
from etils import epath


for f in epath.Path('.').glob('*.dae'):
    t = trimesh.load(f.open('rb'), file_type='dae')
    f_new = f.parent / (f.stem + '_visual' + '.obj')
    b = t.export(f_new.open('w'), file_type='obj')
    f_new.open('w').write(b)
