import os
import re

class TwixFix:
    def __init__(self,input_file):
        self.twix_file = input_file
        self.twix_dump = ''
        self.header_start = ''
    
    def dump_data(self, start_pos=0, nbytes=4096):
        '''
        twix_dump_data(file, nbytes=-1)
          Dump the first nbytes of twix_file header to twix_dump
          Defaults to reading 4096 bytes.
        '''
        if nbytes > 20000 or nbytes == -1:
            print('nbytes too large. resetting.')
            nbytes = 20000
        fid = open(self.twix_file,'rb')
        # start at start_pos relative to beginning of twix file and read a chunk of the header
        fid.seek(start_pos, os.SEEK_SET)
        pos = fid.tell()
        self.twix_dump = fid.read(nbytes)
        fid.close()

    def find_header_start(self):
        '''
        twix_find_header_start(b_twix_data)
          b_twix_data is binary array of twix data (from twix_dump_data)
          returns the byte of the FIRST location in the array of the actual header data
        '''
        if(self.twix_dump):
            #find the entry 'Config', then count backwards to get to the correct start of the file
            pattern = br'Config'
            matches = re.search(pattern, self.twix_dump, re.DOTALL)
            # Config should be at position 8
            new_start_pos = matches.start() - 8
            self.header_start = new_start_pos
        else:
            print('No header info.  Run twix_dump_data first')


    def partial_write(self, output_file, start_pos, max_bytes=-1, overwrite=0):
        '''
        partial_write(self, output_file, start_pos, max_bytes=-1)
         write out a (modified) twix file, based on existing file, but starting at start_pos
         and finishing after max_bytes (if defined)
            output_file = filename for output (will be overwritten if existing)
            start_pos = first byte to write
            max_bytes = max no of bytes to write (for debugging).  Set to -1 to write to end
                        of file, starting at start_pos
            overwrite = [0,1] whether to allow overwrite if output_file exists
               (0 = don't overwrite in any situation, 1 = prompt for overwrite)
        '''

        try:
            open(output_file, 'rb')
            if overwrite == 0:        # overwrite off, so return
                print('File exists and overwrite off.  Skipping ' + self.twix_file)
                return False
            else:                     # overwrite on, check first
                val = input(str(output_file) + " exists.  Overwrite?")
                if val not in [ 'y','Y']:
                    print('Skipping ' + self.twix_file)
                    return False
                else:
                    print ('Writing to ', output_file)                    
        except FileNotFoundError:
                print ('Writing to ', output_file)
            
        with open(self.twix_file, 'rb') as f_in:
            with open(output_file, 'wb') as f_out:
                byte = b'1'
                pos=f_in.seek(start_pos)
                while ( byte and ( pos < max_bytes or max_bytes == -1) ):
                    byte = f_in.read(1)
                    pos = f_in.tell()
                    f_out.write(byte)
                    
        return True



