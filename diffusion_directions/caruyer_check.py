#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
For testing siemensdirclass with Caruyer directions

Created on Wed Feb 14 12:03:10 2024

@author: john
"""

import os, sys
sys.path.append('/Users/john/code/MrDataMethods/diffusion_directions')
import siemensdirclass as dirns

# this takes input from the Caruyer 'multishell' script 


ms = dirns.CaruyerDir('multishell')
ms.read_caruyer('/Users/john/code/qspace/scripts/01-shells-12.txt')
ms.plotbval(1000, 'Caruyer 1 shell, 12 dir')
ms.plotsphere()