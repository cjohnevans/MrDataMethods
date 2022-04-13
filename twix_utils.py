import os
import re

def twix_dump_data(twix_file, start_pos=0, nbytes=4096):
    '''
    twix_dump_data(file, nbytes=-1)
      Dump the first nbytes of twix_file header to twix_dump
      Defaults to reading 4096 bytes.
    '''
    if nbytes > 20000 or nbytes == -1:
        print('nbytes too large. resetting.')
        nbytes = 20000
    fid = open(twix_file,'rb')
    # start at start_pos relative to beginning of twix file and read a chunk of the header
    fid.seek(start_pos, os.SEEK_SET)
    pos = fid.tell()
    twix_dump = fid.read(nbytes)
    fid.close()
    return(twix_dump)

def twix_find_header_start(twix_tmp):
    '''
    twix_find_header_start(b_twix_data)
      b_twix_data is binary array of twix data (from twix_dump_data)
      returns the byte of the FIRST location in the array of the actual header data
    '''
    #find the entry 'Config', then count backwards to get to the correct start of the file
    pattern = br'Config'
    matches = re.search(pattern, twix_tmp, re.DOTALL)
    # Config should be at position 8
    new_start_pos = matches.start() - 8
    return(new_start_pos)

def twix_partial_write(input_file, output_file, start_pos, max_bytes=-1):
    '''
    twix_partial_write(input_file, output_file, start_pos, max_bytes=-1)
        input_file = twix .dat file for input
        output_file = filename for output (will be overwritten if existing)
    '''
    try:
        open(output_file, 'rb')
        val = input(str(output_file) + " exists.  Overwrite?")
        if val not in [ 'y','Y']:
            return False
    except FileNotFoundError:
        print ('Writing to ', output_file)
        
    with open(input_file, 'rb') as f_in:
        with open(output_file, 'wb') as f_out:
            byte = b'1'
            pos=f_in.seek(start_pos)
            while ( byte and pos < max_bytes):
                byte = f_in.read(1)
                pos = f_in.tell()
                print(str(pos), str(byte))
                #f_out.write(byte)

    return True



