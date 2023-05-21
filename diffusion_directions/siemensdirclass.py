# write out a numpy array of values into a siemens dir forma
# array should have format [ [x1, y1, z1], [x2, y2, z2], ... ]

import numpy as np
import matplotlib.pyplot as plt

class SiemensDir:
    def __init__(self, name):
        self.filename = ''
        self.name = name

#  plot functions    
    def plotabs(self):
        print("Name:       ", self.name)
        print("Dimensions: ", self.dims)
        print("Directions: ", self.ndirs)
        print("Vector max :", np.amax(self.gabs))
        print("Vector min :", np.amin(self.gabs))
        tmp = np.unique(self.gabsrnd, False, False, True)
        print("Grad scalings: ", tmp[0])
        print("Number of Dirs:", tmp[1])
        fig =  plt.figure()
        ax1 = fig.add_subplot(1,1,1)
        ax1.plot(self.gabs)
        plt.show()
        
    def plotsphere(self):
        '''
        %matplotlib notebook should go before this call in jupyter to allow interaction in the plot
        '''
        
        xcoord = []
        ycoord = []
        zcoord = []
        for singledir in self.gvec:
            xcoord = np.append(xcoord, singledir[0])
            ycoord = np.append(ycoord, singledir[1])
            zcoord = np.append(zcoord, singledir[2])
        
        # Creating figure
        fig = plt.figure(figsize = (10, 7))
        ax = plt.axes(projection ="3d")
        # Creating plot
        ax.scatter3D(xcoord, ycoord, zcoord, c = self.gabs, cmap = "Set1_r")
        plt.title(self.name)
        plt.gca().set_aspect('equal')
        
    def plotbval(self, maxb, title):
        print("Dimensions: ", self.dims)
        print("Directions: ", self.ndirs)
        print("Vector max :", np.amax(self.gabs))
        print("Vector min :", np.amin(self.gabs))
        # first element is unique grad scalings, second element is number of occurences
        tmp = np.unique(self.gabsrnd, False, False, True)
        print("b values:       ", maxb*np.power(tmp[0],2))
        print("Number of dirs: ", tmp[1])
        fig =  plt.figure()
        ax1 = fig.add_subplot(1,1,1)
        ax1.plot(maxb*np.power(self.gabs,2), 'o-')
        plt.title(self.name)
        plt.show()

# setdir gets the directions from a numpy array (passed from another program)
    def setdir(self, gvec):
        self.gvec = np.array(gvec)
        #print self.gvec
        self.gabs = np.linalg.norm(gvec, None, 1)
        self.gabsrnd = np.around(self.gabs,decimals=3)  #rounded, for checking shells
        self.dims = self.gvec.shape
        print(self.dims[0])
        self.ndirs = self.dims[0]

#add b0 scans every b0gap volumes 
    def addb0(self, b0gap):
        nb0 = np.fix(self.ndirs/b0gap) # num of b0
        newdirs = self.ndirs + nb0
        tempvec = self.gvec
        print(self.ndirs, nb0, newdirs)
        for ii in range(0,int(newdirs), b0gap):
            tempvec = np.insert(tempvec, ii, [ 0, 0, 0 ], axis = 0)
        self.setdir(tempvec)

    def getdir(self):
        return self.gvec
        
# readdirfile gets directions from existing Siemens dir file.
    def readdirfile(self, filename):
        '''
        readdirfile(filename)
        read in a siemens format direction file
        '''
        veclist = []
        ff = open(filename, "r")
        for lne in ff:
            if "vector" in lne:
                vecstr = lne[12:-1].replace('(', '').replace(')','').replace(' ','').replace('\r','')
                vecstr = vecstr.replace('=','').split(',')
                vecflt = [float(j) for j in vecstr]
                veclist.append(vecflt[0:3])   # three values, in case of poorly formatted input file
        vecarr = np.array(veclist)
        self.setdir(vecarr)
        self.filename = filename

# write out in Siemens format
    def writedirfile(self, filename):
        '''
        writedirfile(filename)
           filename - full path to file, otherwise writes to current dir.
        '''
        
        with open(filename, 'w') as fout:
            print("Opened " + filename + " for writing")
            fout.write("# written by siemensdirclass.py  CJE 7/10/21\n\n")
            fout.write("[directions=" + str(self.ndirs) + "]\n")
            fout.write("Normalisation = none\n")
            fout.write("CoordinateSystem = xyz\n\n")
            for ii in range(0,self.ndirs):
                fout.write("vector[" + str(ii) + "] = (" \
                           + "{0:.6f}".format(self.gvec[ii][0]) + "," \
                           + "{0:.6f}".format(self.gvec[ii][1]) + "," \
                           + "{0:.6f}".format(self.gvec[ii][2])  \
                           + ")\n")
                
    def write_ge_customtensor(self, filename):
        '''
        write_ge_customtensor(
           filename
           )
           
        write the gradient directions in a ge custom_tensor format (for GE
        visit in May 2023)   
        '''
        with open(filename, 'w') as fout:
            print("Opened " + filename + " for writing")
            fout.write("# diffqc custom directions (John Evans, May 2023)\n")
            fout.write(str(self.ndirs) + '\n')
            for ii in range(0,self.ndirs):
                fout.write("{0:.5f}".format(self.gvec[ii][0]) + " " \
                           + "{0:.5f}".format(self.gvec[ii][1]) + " " \
                           + "{0:.5f}".format(self.gvec[ii][2])  \
                           + "\n")
        
        
