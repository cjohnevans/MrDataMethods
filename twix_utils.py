import os
import re

def twix_dump_header(twix_file, start_pos, nbytes):
    '''
    twix_dump_header(file, nbytes)
      dump the first nbytes of twix_file header to screen from 
    '''
    fid = open(twix_path,'rb')
    # start at start_pos relative to beginning of twix file and read a chunk of the header
    fid.seek(start_pos, os.SEEK_SET)
    pos = fid.tell()
    hdr = fid.read(nbytes)

    #back to start, and read from 'Config'
    config_start = 8
    fid.seek(config_start, os.SEEK_SET)
    config=fid.read(6)

    print("============ start of header from " + str(twix_file))
    print("pos = " + str(pos))
    print("Config = " + str(config))
#    print(str(hdr))
    return(hdr)

def twix_strip_junk(twix_file):
    '''
    twix_strip_junk(twix_file)
      strip rubbish at the start of twix file header by locating identifiable params in header
    '''

    #get header, starting at file start
    hdr_tmp = twix_dump_header(twix_file, 0, 2048)
    pattern = br'Config'
    


twix_dir = '/cubric/scanners/mri/7t/transfer/314_WAND/'
#work
#twix_1 = '314_17726_2C/meas_MID441_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID115897.dat'
#twix_2 = '314_72783_2C/meas_MID94_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID106545.dat'
#fail
#twix_3 = '314_22482_2C/meas_MID213_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID98696.dat'
#twix_4 = '314_04843_2C/meas_MID135_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID107659.dat'
#twix_5 = '314_08033_2C/meas_MID161_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID93264.dat'
# all_twix = [ twix_1, twix_2, twix_3, twix_4 ]
for ff in all_twix:
    twix_path = os.path.join(twix_dir, ff)
    twix_dump_header(twix_path, 0, 2048)

#bad_mprage_startpos = 1536
#twix_dump_header(twix_path, bad_mprage_startpos, 2048)
