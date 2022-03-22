import sys
sys.path.append('/home/sapje1/code/twixtools')
import twixtools
import os

wand_dir = '/cubric/scanners/mri/7t/transfer/314_WAND/'
mpr_works = '314_17726_2C/meas_MID441_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID115897.dat'
mpr_fails = '314_22482_2C/meas_MID213_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID98696.dat'

mpr_works_path = os.path.join(wand_dir, mpr_works)
mpr_fails_path = os.path.join(wand_dir, mpr_fails)

twix_mpr = twixtools.read_twix(mpr_works_path)
#twix_mpr = twixtools.read_twix(mpr_fails_path)
