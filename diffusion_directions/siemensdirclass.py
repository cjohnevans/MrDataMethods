# write out a numpy array of values into a siemens dir forma
# array should have format [ [x1, y1, z1], [x2, y2, z2], ... ]

import numpy as np
import matplotlib.pyplot as plt

def append_dirs(first_dir_set, second_dir_set):
    '''

    Parameters
    ----------
    first_dir_set : SiemensDir
        First direction direction set.
    
    second_dir_set : SiemensDir
        Second direction direction set to append to first.

    Returns
    -------
    new_dir_set  : SiemensDir
        New direction set with appended directions

    '''
    
    tempvec = first_dir_set.gvec
    print(len(tempvec))
    tempvec = np.append(tempvec, second_dir_set.gvec, axis=0)
    print(len(tempvec))
    new_dir_set = SiemensDir('Appended Directions')
    new_dir_set.setdir(tempvec)
    return(new_dir_set)

class SiemensDir:
    def __init__(self, name, file_name=None):
        if file_name:
            self.filename = filename
            self.readdirfile(self.filename)
        else:
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

    def g_rescale(self, rescale):
        '''
        rescale all values in the gvec 
        '''
        self.setdir(self.gvec * rescale)
        
    def xyzcoord(self):      
        xcoord = []
        ycoord = []
        zcoord = []
        for singledir in self.gvec:
            xcoord = np.append(xcoord, singledir[0])
            ycoord = np.append(ycoord, singledir[1])
            zcoord = np.append(zcoord, singledir[2])
            
        return xcoord, ycoord, zcoord
        
    def set_3plane_plot(self, xcoord, ycoord, zcoord):
        # Creating figure
        fig = plt.figure(figsize = (12, 3))
        ax = fig.subplots(1,3)
        # Creating plot
        ax[0].plot(xcoord,ycoord,'o')
        ax[0].set_xlabel('x')
        ax[0].set_ylabel('y')
        ax[0].set_aspect('equal')
        ax[0].set_xlim(-1,1)
        ax[0].set_ylim(-1,1)
        
        ax[1].plot(xcoord,zcoord,'o')
        ax[1].set_xlabel('x')
        ax[1].set_ylabel('z')
        ax[1].set_aspect('equal')
        ax[1].set_xlim(-1,1)
        ax[1].set_ylim(-1,1)
        
        ax[2].plot(ycoord,zcoord,'o')
        ax[2].set_xlabel('y')
        ax[2].set_ylabel('z')
        ax[2].set_aspect('equal')
        ax[2].set_xlim(-1,1)
        ax[2].set_ylim(-1,1)
        
    def plot_3plane_projections(self):
            
        '''
        %matplotlib notebook should go before this call in jupyter to allow interaction in the plot
        '''   
        xcoord, ycoord, zcoord = self.xyzcoord()
        self.set_3plane_plot(xcoord, ycoord, zcoord)
        
    def plot_3plane_projections_halfsphere(self):
        xcoord, ycoord, zcoord = self.xyzcoord()
        zcoord[zcoord < 0] *= -1
        self.set_3plane_plot(xcoord, ycoord, zcoord)

        
    def plot_sphere(self, half_sphere=False):
        '''
        plot projections along X, Y, Z
        
        half_sphere = True False
            flip the z directions so that all sit on half sphere

        Returns
        -------
        None.

        '''
        xcoord, ycoord, zcoord = self.xyzcoord()
 
#       flip onto half sphere  
        if half_sphere:
            zcoord[zcoord < 0] *= -1
        
        # Creating figure
        fig = plt.figure(figsize = (10, 7))
        
        ax = plt.axes(projection ="3d")
        # Creating plot
        ax.scatter3D(xcoord, ycoord, zcoord, c = self.gabs, cmap = "Set1_r")
        plt.title(self.name)
        plt.gca().set_aspect('equal')
        
        
        return
        
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
                vecflt = [float(j) for j in vecstr[0:3] ]
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
        
class CaruyerDir(SiemensDir):
        
    def __init__(self, name, file_name=None):
        
        self.name = name
        self.shell = []
        
        if file_name:
            self.filename = file_name
            self.read_caruyer(file_name)
        else:
            self.filename = ''
        

    def read_caruyer(self, filename):
        '''
        Read directions from a Caruyer file from https://github.com/ecaruyer/qspace or 
        http://www.emmanuelcaruyer.com/q-space-sampling.php
        '''
        veclist = []
        with open(filename, 'r') as f:
            print("Opened " + filename + " for reading.")
            for line in f:
                if line[0] != '#':
                    txt=line.replace('\n','').split('\t')
                    self.shell.append(int(txt[0]))
                    vecflt = [float(j) for j in txt[1:] ]
                    veclist.append(vecflt[0:3])   # three values, in case of poorly formatted input file
        vecarr = np.array(veclist)
        self.setdir(vecarr)
        self.filename = filename
        self.n_shells = len(np.unique(self.shell))

        print(len(self.shell), len(veclist))
        
    def rescale_caruyer(self, rescale_shell):
        '''
        Parameters
        ----------
        rescale_shell : np.array
            Array of values to rescale the shells.
        
        second_dir_set : SiemensDir
            Second direction direction set to append to first.

        Returns
        -------
        new_dir_set  : SiemensDir
            New direction set with appended directions

        '''
        
        if self.n_shells != len(rescale_shell):
            print('Direction file has ' + str(self.n_shells) + ' shells, but ' + str(len(rescale_shell)) + ' rescales provided.')
            return
        
        rescale = np.array(rescale_shell)
        self.gvec_unitsphere = self.gvec
        newvec = np.empty([self.ndirs,3])
        
        for i in range(self.ndirs):
            newvec[i] = self.gvec_unitsphere[i]*rescale[self.shell[i]]
            print(i, self.shell[i], newvec[i])
        print(newvec)            

        
        

