import glob
import siemensdicom
import os

dcm_dir = '/home/sapje1/data_sapje1/2022/fmri_param_check/singledicoms/'
dcm_file = glob.glob(dcm_dir + '*-1-*')
print(dcm_file)

dcmhdr = siemensdicom.SiemensDicom()
dcmhdr.read_dicom(dcm_file)
dcmhdr.show_dicom_field('all')
dcmhdr.show_unformatted()
