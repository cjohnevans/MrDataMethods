from pydicom import dcmread
import os

class SiemensDicom:
    '''
    class for handling dicom header info from a single dicom file
    '''
    def __init__(self, input_file):
        self.n_dicoms = 0
        self.input_file = input_file
        self.dcm = []   #list of dicts
        self.dcm_file = []
        self.field_lookup = { 'scanner': (0x0008, 0x0080), \
                         'study_date': (0x0008, 0x0020), \
                         'study_time': (0x0008, 0x0030), \
                         'study_description': (0x0008, 0x1030), \
                         'protocol': (0x0040, 0x0254), \
                         'series_description': (0x0008, 0x103e), \
                         'patient_id': (0x0010, 0x0010), \
                         'study_id': (0x0010, 0x0020), \
                         'comments': (0x0010, 0x4000), \
                         'sequence': (0x0018, 0x0024), \
                         'tr': (0x0018, 0x0080), \
                         'te': (0x0018, 0x0081), \
                         'ti': (0x0018, 0x0082), \
                         'flip_angle': (0x0018, 0x1314), \
                         'slice_thk': (0x0018, 0x0050), \
                         'slice_spc': (0x0018, 0x0088), \
                         'npe': (0x0018, 0x0089), \
                         'necho': (0x0018, 0x0086), \
                         'ipat': (0x0051, 0x1011),\
                         'etl': (0x0018, 0x0091), \
                         'phase_fov': (0x0018, 0x0094), \
                         'px_space': (0x0028, 0x0030), \
                         'px_bw_rd': (0x0018, 0x0095), \
                         'acq_mtx': (0x0018, 0x1310), \
                         'px_bw_pe': (0x0019, 0x1028), \
                         'comments': (0x0020, 0x4000),\
                         'txcoil': (0x0018, 0x1251),\
                         'rxcoil': (0x0051, 0x100f), \
                         'b_value': (0x0019, 0x100c), \
                         'diff_gradients': (0x0019, 0x100e) \
                         }
        self.read_dicom()

    # currently reads a single file, but some syntax assumes multi-file compatiblity
    #  Need to decide on whether single or multi is more logical.
    def read_dicom(self):
        if '.dcm' in self.input_file:
            self.dcm.append(dcmread(self.input_file))
            self.dcm_file.append(self.input_file)

    # assumes single file in the SiemensDicom object
    def show_dicom(self):
        '''
        print dicom info from one of the dicom files loaded
        shows verbose list of fields.
        '''
        print('>>>', self.dcm_file, '>>>')
        self.show_dicom_field('all')


    def show_dicom_field(self, fields):
        '''
        show single dicom field
        '''     
        field_value = []
        for dd in self.dcm:
            if fields == 'all': #all fields
                for printfield in self.field_lookup:
                    try:
                        print(dd[self.field_lookup[printfield]])
                        field_value.append(dd[self.field_lookup[printfield]])
                    except:
                        print('DICOM field ', printfield, ' not found')
            elif len(fields) == 1:   #single field
                try:
                    print(dd[self.field_lookup[fields[0]]])
                    field_value.append(dd[self.field_lookup[fields[0]]])
                except:
                    print('DICOM field ', printfield, ' not found')
            else:    #only loop for multiple values in list
                for printfield in fields:
                    try:
                        print(dd[self.field_lookup[printfield]])
                        field_value.append(dd[self.field_lookup[printfield]])
                    except:
                        print('DICOM field ', printfield, ' not found')
        return(field_value)

    def show_unformatted(self):
        for dd in self.dcm:
            print(dd)
            print(dir(dd))
            #print(dd[(0x0029, 0x1010)].value) # this looks like the CSA header - needs parsing

#    def change_dicom_field(self,

class MultiSiemensDicom:
    '''
    class for handling multiple dicom files, from a common file path root
    '''
    def __init__(self, dcm_path_top):
        self.dcm_path = dcm_path_top
        self.dcm_file_list = []
        for [root, dirs, files] in os.walk(self.dcm_path):
            for file in files:
                if '.dcm' in file:
                    self.dcm_file_list.append(os.path.join(root, file))
        self.n_dcm = len(self.dcm_file_list)
        self.dicom_files = []
        for file in self.dcm_file_list:
            self.dicom_files.append(SiemensDicom(file))

    def show_dcm_list(self):
        print(self.dcm_file_list)
        print("Found " + str(self.n_dcm) + " dicoms")

    def get_field(self, dicom_field):
        '''
        get dicom field values for all dicoms in MultiSiemensDicom object
        dicom_field should be a list.
        '''
        field_values = []
        
        try:
            for dcm in self.dicom_files:
                field_values.append(dcm.show_dicom_field(dicom_field))
        except:
            print('dicom field not found')
        #field_values_unique = set(field_values)
        print(field_values)
