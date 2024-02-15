#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
For testing siemensdirclass with Caruyer directions

Created on Wed Feb 14 12:03:10 2024

@author: john
"""

import os, sys
#sys.path.append('/Users/john/code/MrDataMethods/diffusion_directions')
sys.path.append('/home/sapje1/code/python_mrobjects/diffusion_directions')
import siemensdirclass as dirns

ms = dirns.CaruyerDir('multishell')
#ms.read_caruyer('/Users/john/code/temp.txt')
ms.read_caruyer('/home/sapje1/code/qspace/scripts/03-shells-60-60-60.txt')

ms.plotbval(1000, 'test')
ms.plotsphere()