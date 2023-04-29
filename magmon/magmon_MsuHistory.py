'''
MsuHistory.dat needs to be transferred from scanners via some mechanism
For Connectom this can be done as a scheduled task set up on the 
scanner host.
Format of dat file is four lines per measurement;
   -date
   -header
   -data
   -dashes
'''


import pandas as pd
import sys
import os
import matplotlib.pyplot as plt

pd.options.display.max_colwidth=200

magmon_output_path = '/home/sapje1/data_sapje1/magmon/connectom'

def splash():
    print('\nmagmon_MsuHistory.py')
    print('   Read MsuHistory for magnet temperatures, pressures and')
    print('   Helium level from Connectom and Prisma systems.\n')
    print('   USAGE:        python path_to_magmon/magmon_MsuHistory.py MSU_HISTORY.DAT')
    print('   ARGUMENTS:    MSU_HISTORY.DAT - history file to analyse\n')

# argv[0] is command, argv[1] .. argv[n] are arguments
if len(sys.argv) < 2:
    splash()
    sys.exit()
if not os.path.exists(sys.argv[1]):
    print("Can't find file " + sys.argv[1])
    sys.exit()
else:
    msu_file = sys.argv[1]

print(msu_file)
with open(msu_file,'r') as f:
    msu_str=f.readlines()

# get string date into datetime (to use as pd index)
msu_date = msu_str[::4]
date = [ d.replace('\n','').replace(' ','_') for d in msu_date ]
date_pd = pd.to_datetime(date, format="%Y-%m-%d_%H:%M:%S")

# deal with oddly-formatted column headings
msu_hdr = msu_str[1].split('|')
msu_hdr2 = [ h.strip() for h in msu_hdr ]

# finally, the data
msu_dat = msu_str[2::4]
msu_dat2 = []
for d in msu_dat:
    dspl=d.split('|')
    dsplstr = [ a.strip() for a in dspl ]
    msu_dat2.append(dsplstr)

# into pandas
msu_pd = pd.DataFrame(msu_dat2,columns=msu_hdr2,index=date_pd, dtype=float)

date_out = '{:%Y-%m-%d_%H%M%S}'.format(msu_pd.index[-1])
msu_pd.to_csv(os.path.join(magmon_output_path,'msu_history.csv'))
msu_pd.to_csv(os.path.join(magmon_output_path,date_out+'_msu_history.csv'))


msu_pd.plot(y=['dColdHeadTemperature','dBoreTemperature','dLinkTemperature'],title='Temperatures (K)')
plt.savefig(os.path.join(magmon_output_path,'cryo_temps.png'))

msu_pd.plot(y=['dMagnetPressure'],title='Helium pressure (bar)')
plt.savefig(os.path.join(magmon_output_path,'He_press.png'))

msu_pd.plot(y=['HeliumLevel'],title='Helium level (%)')
plt.savefig(os.path.join(magmon_output_path,'He_level.png'))
