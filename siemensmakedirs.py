# read in elec120 from camino and set up for Connectom

import numpy as np
import matplotlib.pyplot as plt
from siemensdirclass import SiemensDir
caminofile = open("Elec120.txt",'r')
caminofile = open("gradset_120.txt",'r')


ii=0
dirX = []
dirY = []
dirZ = []
rsqr = []

while True:
   nextline = caminofile.readline()
   nextline = nextline[0:-1]
   if len(nextline) == 0:
      break
   else:
# this bit for Elec120 (1 column)
#      xyz = np.mod(ii,3) # X=0, Y=1, Z=2 
#      if xyz == 0:
#         dirX.append(nextline)
#      if xyz == 1:
#         dirY.append(nextline)
#      if xyz == 2:
#         dirZ.append(nextline)
# this bit for gradset_120 (3 cols)
       vecstr=nextline.split()
       dirX.append(vecstr[0])
       dirY.append(vecstr[1])
       dirZ.append(vecstr[2])
   ii=ii+1

elec120_vec = np.column_stack((dirX, dirY, dirZ))

elec120dir = SiemensDir()
elec120dir.setdir(elec120_vec)
#elec120dir.addb0(20)
#elec120dir.writedirfile()
elec120dir.plotabs()


mshardidir = SiemensDir()
#newdir.readdirfile("ALSPAC2_1200_6000_30000.dir")
mshardidir.readdirfile("ALSPAC2.dir")
#mshardidir.plotbval(6000)

# take b=1200 and b=6000 shells only
mshardivec = mshardidir.getdir()
b1200vec = mshardivec[0:32]
b6000vec = mshardivec
b6000vec = np.delete(b6000vec, np.s_[1:202], axis=0)
print "shape: ", b6000vec.shape
print b6000vec[-1]
print mshardivec[-1]
b1200b6000vec = np.append(b1200vec, b6000vec, axis=0)
# remove b0s
# b0s at 0,1,32, 33, 54, 76
b1200b6000vec = np.delete(b1200b6000vec, 76,0);
b1200b6000vec = np.delete(b1200b6000vec, 54,0);
b1200b6000vec = np.delete(b1200b6000vec, 33,0);
b1200b6000vec = np.delete(b1200b6000vec, 32,0);
b1200b6000vec = np.delete(b1200b6000vec, 1,0);
b1200b6000vec = np.delete(b1200b6000vec, 0,0);
#setup SiemensDir object for b=1200, 6k
b1200b6000dir = SiemensDir()
b1200b6000dir.setdir(b1200b6000vec)
b1200b6000dir.plotbval(6000)

#rescale for a max bval of 30k, rather than original 6k
b_scale = np.sqrt(6.0/30.0)
b1200b6000vec = b1200b6000vec*b_scale
#add elec120 directions at b=30k (scaled to r=1)
b1200_6k_30kvec = np.append(b1200b6000vec, elec120_vec, axis=0)
# shuffle
#print b1200_6k_30kvec
np.random.shuffle(b1200_6k_30kvec)
#print b1200_6k_30kvec
b1200_6k_30k = SiemensDir()
b1200_6k_30k.setdir(b1200_6k_30kvec)
b1200_6k_30k.addb0(20)
#write to dir file
b1200_6k_30k.writedirfile()
b1200_6k_30k.plotbval(30000)









