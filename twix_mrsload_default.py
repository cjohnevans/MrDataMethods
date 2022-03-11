# works for prisma gaba data
# doesn't work for 7T (VB) data, Minnesota sequence

import sys
sys.path.append('/home/sapje1/code/suspect')
import suspect
import numpy as np
from matplotlib import pyplot as plt
import os

data_dir = '/home/sapje1/data_sapje1/projects/wand/mrs/19_06_14-11_17_09-DST-1_3_12_2_1107_5_2_43_66073/scans/502-RAW_anonymised/resources/TWIX/files'
twix_file = 'meas_MID00465_FID13471_mpress_AC_met.dat'
full_path = os.path.join(data_dir, twix_file)

twix_data = suspect.io.twix.load_twix(full_path)
# shape of twix data is (edit_on/edit_off, average, Rx_channel, n_points)
print(twix_data)
print(twix_data.shape)
print(type(twix_data))

# for edited data, deal with edit on/ edit off separately
# channel0 is edit off, channel1 is edit on
comb_channels0 = suspect.processing.channel_combination.combine_channels(twix_data[0])
comb_channels1 = suspect.processing.channel_combination.combine_channels(twix_data[1])
avg_comb_channels0 = np.mean(comb_channels0,0)
avg_comb_channels1 = np.mean(comb_channels1,0)
f_ppm = avg_comb_channels0.frequency_axis_ppm()

# plot the results of combining and averaging 
fig,ax = plt.subplots()
ax.plot(f_ppm, np.real(1e5*avg_comb_channels0.spectrum()), \
        f_ppm, np.real(1e5*avg_comb_channels1.spectrum()))
ax.set_xlim(4.5,1)
ax.set_ylim(-3,25)
plt.show()
