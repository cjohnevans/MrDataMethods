from pydicom import dcmread
import os
import matplotlib.pyplot as plt
import glob
import siemensdicom

scan_dir_name = '/home/sapje1/data_sapje1/MuhamedErick/17_09_26-17_14_51-DST-1_3_12_2_1107_5_2_0_19950/'
bvals = []
graddirs = []
filelist = glob.glob(scan_dir_name + '/*/DICOM/*-3-*')   #full paths to first images in all dicom dirs.
excludefiles = ['TRACEW', 'mprage', 'REF_PA', 'localizer']  #partial string matches to exclude
filterfilelist = []

# filter the excludefiles partial string matches
for file in filelist:  
    include_dir = True
    for exclude in excludefiles:
        if exclude in file:
            include_dir = False
    if include_dir:
        filterfilelist.append(file)

filterfilelist.sort()
dcmhdr = siemensdicom.SiemensDicom()
dcmhdr.read_dicom(filterfilelist)

for show_file_idx in range(0,len(filterfilelist)):
    print(filterfilelist[show_file_idx])
    dcmhdr.show_dicom_field(show_file_idx, ['ti', 'te', 'b_value'])


