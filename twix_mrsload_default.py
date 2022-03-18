'''
twix_mrsload_default(path, file)



'''

import sys
sys.path.append('/home/sapje1/code/suspect')
import suspect
import numpy as np
from matplotlib import pyplot as plt
import os

def basic_preproc(mrs_data):
    '''
    in this case data is an MRSdata object for a single acquisition type
    e.g. all data for unedited, edit-on or edit-off only for edited
    should have three dimensions - averages, channels, points

    preprocessing steps:
    - combine channels
    - average across repetitions
    - phase correction
     
    '''
    comb_channels = suspect.processing.channel_combination.combine_channels(mrs_data)
    avg_comb = np.mean(comb_channels,0)
    phase_est = suspect.processing.phase.mag_real(avg_comb,(),(0.0, 6.0))
    return avg_comb.adjust_phase(phase_est[0],phase_est[1],0) 
    
# wand 3T MRS
data_dir = '/home/sapje1/data_sapje1/projects/wand/mrs/19_06_14-11_17_09-DST-1_3_12_2_1107_5_2_43_66073/scans/502-RAW_anonymised/resources/TWIX/files'
in_file = 'meas_MID00465_FID13471_mpress_AC_met.dat'
#covid bbb brainstem 7t cubric pilot
data_dir = '/home/sapje1/data_sapje1/projects/covidbbb'
in_file = [ 'pilot220315/meas_MID165_sLaser_Brainstem_20_12_12_FID118913.dat', \
            'oxford017/meas_MID156_sLaser_Brainstem_20_12_12_FID7821.dat', \
            'oxford018/meas_MID112_sLaser_Brainstem_20_12_12_FID8065.dat']

if type(in_file) is str:
    in_file_list = [ in_file ]  # make it a list
    print(type(twix_file))
elif type(in_file) is list:
    in_file_list = in_file
    
preproc_mrsdata = []  # a list of MRSData objects
for file in in_file_list:
    full_path = os.path.join(data_dir, file)
    print('Loading ' + full_path)
    twix_data = suspect.io.twix.load_twix(full_path)
    # shape of twix data is (edit_on/edit_off, average, Rx_channel, n_points) for edited data
    #  (average, Rx_channel, n_points) for unedited data
    print(twix_data.shape)
    if twix_data.ndim == 3:
        # it's unedited
        is_edited = False
        preproc_mrsdata.append(basic_preproc(twix_data))
    if twix_data.ndim == 4:
        # for edited data, deal with edit on/ edit off separately
        #  channel0 is edit off, channel1 is edit on
        is_edited = True
        for i in range(0,2):
            preproc_mrsdata.append(basic_preproc(twix_data[i]))
    print(type(preproc_mrsdata))


f_ppm = preproc_mrsdata[0].frequency_axis_ppm()
# plot the results of combining and averaging 
fig,ax = plt.subplots()
offset = 0
scale = 1e5
offset = 10
ii=0
for dat in preproc_mrsdata:
    ax.plot(f_ppm, np.real(scale*dat.spectrum() + (ii*offset) ) )
    ii = ii + 1
ax.set_xlim(6,0)
#ax.set_ylim(-3,25)
plt.show()
