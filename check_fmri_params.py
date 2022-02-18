import glob
import siemensdicom
import os

dcm_dir = '/home/sapje1/data_sapje1/2022/fmri_param_check/18_05_29-14_52_23-DST-1_3_12_2_1107_5_2_43_66073/scans/3-3_1_Functionalodditylocaliser_mb4_RUN1/resources/DICOM/files/'
dcm_file = glob.glob(dcm_dir + '*-1-*')
print(dcm_file)

dcmhdr = siemensdicom.SiemensDicom()
dcmhdr.read_dicom(dcm_file)
dcmhdr.show_dicom_field(0, 'all')
#dcmhdr.show_unformatted()
