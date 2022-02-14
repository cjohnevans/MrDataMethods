from pydicom import dcmread

class SiemensDicom:
    def __init__(self):
        self.n_dicoms = 0
        self.dcm = []   #list of dicts
        self.dcm_file = []

    def read_dicom(self, file_list):
        self.n_dicoms = len(file_list)
        for file in file_list:
            if '.dcm' in file:
                self.dcm.append(dcmread(file))
                self.dcm_file.append(file)
        print(file_list[0])

    def show_dicom(self, dicom_no):
        '''
        print dicom info from one of the dicom files loaded
        shows verbose list of fields.
        '''
        print('>>>', self.dcm_file[dicom_no], '>>>')
        self.show_dicom_field(dicom_no, 'all')


    def show_dicom_field(self, dicom_no, fields):
        '''
        show single dicom field
        '''
        field_lookup = { 'scanner': (0x0008, 0x0080), \
                         'study_date': (0x0008, 0x0020), \
                         'study_time': (0x0008, 0x0030), \
                         'study_description': (0x0008, 0x1030), \
                         'series_description': (0x0008, 0x103e), \
                         'patient_id': (0x0010, 0x0010), \
                         'study_id': (0x0010, 0x0020), \
                         'comments': (0x0010, 0x4000), \
                         'sequence': (0x0018, 0x0024), \
                         'tr': (0x0018, 0x0080), \
                         'te': (0x0018, 0x0081), \
                         'ti': (0x0018, 0x0082), \
                         'flip_angle': (0x0018, 0x1314), \
                         'b_value': (0x0019, 0x100c), \
                         'diff_gradients': (0x0019, 0x100e) \
                         }
        ##grad_vec_length = []
        ##
        ##for vec in graddirs:
        ##    print(vec)
        ##    grad_vec_length.append( ( vec[0]**2 + vec[1]**2 + \
        ##                              vec[2]**2 ) ** (1/2) )
        
        if fields == 'all': #all fields
            for printfield in field_lookup:
                try:
                    print(self.dcm[dicom_no][field_lookup[printfield]])
                except:
                    print('DICOM field ', printfield, ' not found')
        elif len(fields) == 1:   #single field
            try:
                print(self.dcm[dicom_no][field_lookup[fields[0]]])
            except:
                print('DICOM field ', printfield, ' not found')
        else:    #only loop for multiple values in list
            for printfield in fields:
                try:
                    print(self.dcm[dicom_no][field_lookup[printfield]])
                except:
                    print('DICOM field ', printfield, ' not found')

        
