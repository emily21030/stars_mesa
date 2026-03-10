import os
import numpy as np
import subprocess
import time

mass = np.array([0.9, 0.8, 0.7, 0.6])
# mass = np.linspace(49, 1, 49)
# mass = np.linspace(40, 10, 4)
# mass = np.delete(mass, np.where(mass == 40))
# mass = np.delete(mass, np.where(mass == 30))
# mass = np.delete(mass, np.where(mass == 20))
# mass = np.delete(mass, np.where(mass == 1))
# mass = np.linspace(50, 50, 1)

for m in mass:
    os.chdir("iso_0"+str(m)+"M")
    # subprocess.call("~/docker_work/isochrones/iso_"+str(m)+"M/mk", shell=True)
    subprocess.call("./mk", shell=True)
    os.chdir("photos")
    last_photo = sorted(os.listdir())[-1]
    os.chdir("..")
    print("running iso_"+str(m)+"M from photo " + str(last_photo))
    start = time.time()
    # subprocess.call("~/docker_work/isochrones/iso_"+str(m)+"M/rn", shell=True)
    # subprocess.call("./rn", shell=True)
    subprocess.call("./re "+str(last_photo), shell=True)
    end = time.time()
    print("iso_"+str(m)+"M complete")
    print("time taken: ", end-start)
    os.chdir("..")