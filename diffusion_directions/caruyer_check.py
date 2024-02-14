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

ms = dirns.CaruyerDir('multishell')
ms.read_caruyer('/Users/john/code/temp.txt')
ms.plotbval(1000, 'test')
ms.plotsphere()