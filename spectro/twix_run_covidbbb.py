#!/usr/bin/env python
# coding: utf-8

# In[1]:
import sys
sys.path.append('/home/sapje1/code/python_mrobjects')
import twixmrs


# In[2]:


# wand 3T MRS
data_dir = '/home/sapje1/data_sapje1/projects/wand/mrs/19_06_14-11_17_09-DST-1_3_12_2_1107_5_2_43_66073/scans/502-RAW_anonymised/resources/TWIX/files'
in_file = 'meas_MID00465_FID13471_mpress_AC_met.dat'
#covid bbb brainstem 7t cubric pilot
data_dir = '/home/sapje1/data_sapje1/projects/bbbcovid'
in_file = [ '220315_pilot/meas_MID165_sLaser_Brainstem_20_12_12_FID118913.dat',\
            '220401_pilot/meas_MID199_sLaser_Brainstem_20_12_12_FID120393.dat',\
             'oxford017/meas_MID156_sLaser_Brainstem_20_12_12_FID7821.dat',\
             'oxford018/meas_MID112_sLaser_Brainstem_20_12_12_FID8065.dat',
             'CAU002N01/meas_MID68_sLaser_Brainstem_20_12_12_FID121048.dat' ]
#in_file = ['220315_pilot/meas_MID165_sLaser_Brainstem_20_12_12_FID118913.dat']


# In[3]:


print(in_file)
mrs_data = twixmrs.twixmrs_load_basic(data_dir, in_file)


# In[7]:

mrs_data_phased = []
mrs_data_phased.append( mrs_data[0].adjust_phase(-0.4,0.0015) )  #cubric_220315
mrs_data_phased.append( mrs_data[1].adjust_phase(-0.4,0.0015) )  #cubric_220315
mrs_data_phased.append( mrs_data[4].adjust_phase(-0.4,0.0015) )  # CAU002N01
mrs_data_phased.append( mrs_data[2].adjust_phase(-0.5,0.002))   # oxford 017
mrs_data_phased.append( mrs_data[3].adjust_phase(-0.5,0.002))   # oxford 018

line_label = ['CUBRIC_220315', 'CUBRIC_220401', 'CAU002N001', 'Oxford_017','Oxford_018']
twixmrs.twixmrs_plot(mrs_data_phased, line_label)


# In[5]:
