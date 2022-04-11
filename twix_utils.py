import os
import re

def twix_dump_data(twix_file, start_pos=0, nbytes=4096):
    '''
    twix_dump_data(file, nbytes=-1)
      Dump the first nbytes of twix_file header to twix_dump
      Defaults to reading 4096 bytes.
    '''
    print(nbytes)
    if nbytes > 20000 or nbytes == -1:
        print('nbytes too large. resetting.')
        nbytes = 20000
    print(nbytes)
    fid = open(twix_file,'rb')
    # start at start_pos relative to beginning of twix file and read a chunk of the header
    fid.seek(start_pos, os.SEEK_SET)
    pos = fid.tell()
    twix_dump = fid.read(nbytes)
    fid.close()
    return(twix_dump)

def twix_strip_junk(twix_tmp):
    '''
    '''
    #find the entry 'Config', then count backwards to get to the correct start of the file
    pattern = br'Config'
    matches = re.search(pattern, twix_tmp, re.DOTALL)
    # Config should be at position 8
    new_start_pos = matches.start() - 8
    twix_out = bytearray(twix_tmp[new_start_pos:])
    return(twix_out)

def twix_strip_write(input_file, output_file, max_bytes=-1):
    '''
    twix_strip_junk(twix_file)
        input_file = twix .dat file for input
        output_file = filename for output (will be overwritten if existing)
        strip rubbish at the start of twix file header by locating identifiable params in header
        read data from input_file and write to output_file bytewise
    '''
    try:
        open(output_file, 'rb')
        print("Writing to ", output_file);
    except FileNotFoundError:
        print(output_file, "exists.  Try a different file name")
        return False
        

    orig_header = twix_dump_data(input_file)
    #find the entry 'Config', then count backwards to get to the correct start of the file
    pattern = br'Config'
    matches = re.search(pattern, orig_header, re.DOTALL)
    # Config should be at position 8
    new_start_pos = matches.start() - 8

    with open(input_file, 'rb') as f_in:
        with open(output_file, 'wb') as f_out:
            byte = b'1'
            f_in.seek(new_start_pos)
            while byte:
                byte = f_in.read(1)
                f_out.write(byte)

    return True



