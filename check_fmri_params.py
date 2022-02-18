import glob
import siemensdicom
import os

dcm_dir = '/home/sapje1/data_sapje1/2022/fmri_param_check/singledicoms/'
dcm_files = glob.glob(dcm_dir + '*-1-*')
print(dcm_files)

dcmhdr = siemensdicom.SiemensDicom()
dcmhdr.read_dicom(dcm_files)
#dcmhdr.show_dicom_field('all')
dcmhdr.show_dicom_field_parser()

#dcmhdr.show_unformatted()
