import os
import numpy as np
import matplotlib.pyplot as plt
from bart import bart
import twixtools
from utils import convert_to_cfl


class twix_map():
    def __init__(self, twixfile):
        '''
    
        Parameters
        ----------
        twixfile : TYPE, optional
            DESCRIPTION. Read a twixfile using twixtools. Makes no assumptions
            about the components within the twix file
    
        Returns
        -------
        twix_map (a list of dicts of twixtools twix_array objects)
    
        '''
        
        self.map = twixtools.map_twix(twixfile)
    
    def show_top_level(self):
        print("Map has " + str(len(self.map)) + " top level objects:")
        for i in self.map:
            print(i.keys())
            
    def show_info(self):
        print("Map has " + str(len(self.map)) + " top level objects:")
        o_num = 0
        for o in self.map:
            print("object: " + str(o_num))
            for k in o:
                if "hdr" not in k:
                    print(k, o[k].base_size) 
            o_num=o_num+1

    def prep_k_space(twix_map, removeos=False, apply_phasecor=False):
        return null
    

