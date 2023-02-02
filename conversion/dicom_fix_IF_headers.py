#  fix the headers of the dicom data for transfer to telemedclinic
#   change the patient_id to a 'CUBRyynnn' ID and add an accession no

import sys
import siemensdicom
import os
sys.path.append('/home/sapje1/code/python_mrobjects')

dcm_list = []

##dcm_path_top = '/home/sapje1/Downloads/checkif/junk'
##for [root, dirs, files] in os.walk('/home/sapje1/Downloads/checkif/junk'):
##    for file in files:
##        if '.dcm' in file:
##            dcm_list.append(os.path.join(root, file))
##
##print(dcm_list)
##print("Found " +  str(len(dcm_list)) + " dicom files")

#for dcm_file in dcm_list:
#    print(dcm_file)
#    one_dcm = siemensdicom.SiemensDicom(dcm_file)
#    one_dcm.show_dicom_field(['patient_id'])

all_dicoms = siemensdicom.MultiSiemensDicom('/home/sapje1/Downloads/checkif/junk')
all_dicoms.show_dcm_list()
all_dicoms.get_field(['patient_id'])
