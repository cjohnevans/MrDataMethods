#  this is the script version

import sys
sys.path.append('/home/sapje1/code/suspect')
import suspect
import numpy as np
from matplotlib import pyplot as plt
import os

def basic_combine_mean(mrs_data):
    '''
    in this case data is an MRSdata object for a single acquisition type
    e.g. all data for unedited, edit-on or edit-off only for edited
    should have three dimensions - averages, channels, points
    '''
    comb_channels = suspect.processing.channel_combination.combine_channels(mrs_data)
    return np.mean(comb_channels,0)
    
# wand 3T MRS
data_dir = '/home/sapje1/data_sapje1/projects/wand/mrs/19_06_14-11_17_09-DST-1_3_12_2_1107_5_2_43_66073/scans/502-RAW_anonymised/resources/TWIX/files'
twix_file = 'meas_MID00465_FID13471_mpress_AC_met.dat'
#covid bbb brainstem 7t cubric pilot
#data_dir = '/home/sapje1/data_sapje1/projects/covidbbb/pilot220315'
#twix_file = 'meas_MID165_sLaser_Brainstem_20_12_12_FID118913.dat'
full_path = os.path.join(data_dir, twix_file)

twix_data = suspect.io.twix.load_twix(full_path)
# shape of twix data is (edit_on/edit_off, average, Rx_channel, n_points) for edited data
#  (average, Rx_channel, n_points) for unedited data
print(twix_data.shape)

preproc_mrsdata = []  # a list of MRSData objects
if twix_data.ndim == 3:
    # it's unedited
    is_edited = False
    preproc_mrsdata = [ basic_combine_mean(twix_data) ]
if twix_data.ndim == 4:
    # for edited data, deal with edit on/ edit off separately
    #  channel0 is edit off, channel1 is edit on
    is_edited = True
    for i in range(0,2):
        preproc_mrsdata.append(basic_combine_mean(twix_data[i]))

print(type(preproc_mrsdata))        
f_ppm = preproc_mrsdata[0].frequency_axis_ppm()

# plot the results of combining and averaging 
fig,ax = plt.subplots()
ax.plot(f_ppm, np.real(1e5*preproc_mrsdata[0].spectrum()))
ax.plot(f_ppm, np.real(1e5*preproc_mrsdata[1].spectrum()))
ax.set_xlim(5.5,1)
ax.set_ylim(-3,25)
plt.show()
