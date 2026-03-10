import numpy as np
import shutil

mass = np.linspace(1.4, 0.7, 8)
# mass = np.linspace(49, 1, 49)
# mass = np.linspace(40, 10, 4)
# mass = np.linspace(49.5, 49.5, 1)
# mass = np.delete(mass, np.where(mass == 1))
mass = np.array([0.5, 1.0, 1.5])

for m in mass:
    # shutil.rmtree(f'iso_{m:.1f}M')
    # shutil.copytree('base', f'iso_{m:.1f}M')
    lines = []
    with open(f'iso_0{m:.1f}M/inlist_project','r') as f:
        for line in f:
            lines.append(line)
        lines[70] = f"  force_timestep_min_years = 1d5\n"
        # lines[53] = f"    xa_central_lower_limit(1) = 1d-10\n"
        # lines[55] = ""
        # lines[69] = f"  min_timestep_limit = 1e6 ! in seconds\n"
    with open(f'iso_0{m:.1f}M/inlist_project','w') as f:
        for line in lines:
            f.write(line)