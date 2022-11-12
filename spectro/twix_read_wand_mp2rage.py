import sys
sys.path.append('/home/sapje1/code/twixtools')
import twixtools
import os

wand_dir = '/cubric/scanners/mri/7t/transfer/314_WAND/'
mpr1 = ['314_17726_2C/meas_MID441_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID115897.dat' ]
twix_works_hdr = []
for twx in mpr1:
    mpr1_path = os.path.join(wand_dir, twx)

twix_works = twixtools.read_twix(mpr1_path)
twix_works_hdr.append(twix_works[0]['hdr'])
