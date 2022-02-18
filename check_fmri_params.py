import glob
import siemensdicom
import os

dcm_dir = '/home/sapje1/data_sapje1/2022/fmri_param_check/singledicoms/'
dcm_files = glob.glob(dcm_dir + '*-1-*')
dcm_files = [dcm_dir + '1.3.12.2.1107.5.2.43.66073.30000017051708095386700000052-8-1-54rno2.dcm']
print(dcm_files)

dcmhdr = siemensdicom.SiemensDicom()
dcmhdr.read_dicom(dcm_files)
#dcmhdr.show_dicom_field('all')
dcmhdr.show_dicom_field_parser()

#dcmhdr.show_unformatted()
