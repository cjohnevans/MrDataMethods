import sys
sys.path.append('/home/sapje1/code/python_mrobjects')
import siemensdirclass as sd

checkdir = sd.SiemensDir()
checkdir.readdirfile('Sph61Opt.dir')
checkdir.plotbval(1,'Sph61Opt.dir (b=2400,4000,6000)')

checkdir2 = sd.SiemensDir()
checkdir2.readdirfile('Jones31.dir')
checkdir2.plotbval(1, 'Jones31.dir (b=500,1200)')
