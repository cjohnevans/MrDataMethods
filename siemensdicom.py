from pydicom import dcmread
from dicom_parser import Image


class SiemensDicom:
    def __init__(self):
        self.n_dicoms = 0
        self.dcm = []   #list of dicts
        self.dcm_p = []   
        self.dcm_file = []

    def read_dicom(self, file_list):
        self.n_dicoms = len(file_list)
        for file in file_list:
            print(file)
            if '.dcm' in file:
                # using pydicom
                self.dcm.append(dcmread(file))
                self.dcm_file.append(file)
                # using dicom_parser
                self.dcm_p.append(Image(file))
        print(file_list[0])


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
        field_lookup = { 'scanner': (0x0008, 0x0080), \
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
        ##grad_vec_length = []
        ##
        ##for vec in graddirs:
        ##    print(vec)
        ##    grad_vec_length.append( ( vec[0]**2 + vec[1]**2 + \
        ##                              vec[2]**2 ) ** (1/2) )
        
        for dd in self.dcm:
            if fields == 'all': #all fields
                for printfield in field_lookup:
                    try:
                        print(dd[field_lookup[printfield]])
                    except:
                        print('DICOM field ', printfield, ' not found')
            elif len(fields) == 1:   #single field
                try:
                    print(dd[field_lookup[fields[0]]])
                except:
                    print('DICOM field ', printfield, ' not found')
            else:    #only loop for multiple values in list
                for printfield in fields:
                    try:
                        print(dd[field_lookup[printfield]])
                    except:
                        print('DICOM field ', printfield, ' not found')

    def show_unformatted(self):
        for dd in self.dcm:
            print(dd)
            print(dir(dd))
            print(dd[(0x0029, 0x1010)].description)

    def show_dicom_field_parser(self):
        print(len(self.dcm_p))
        for dd in self.dcm_p:
            print(dd.header.get('EchoTime'))
            #print(dd.header)

        
