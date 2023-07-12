# get data from the Hyperfine raw data server (hfrds)
import os
import subprocess

data_path_local = '/home/sapje1/scratch_sapje1/2023/230712_hyperfine_raw'
data_path_hfrds = '/home/rrdf/RRDF'

print('hello')

subprocess.run(['ls','-1'])
# get dir listing from hfrds
raw_exam=subprocess.run(['ssh','-XY','-p','25125','rrdf@10.186.64.34','ls',data_path_hfrds])
print(type(raw_exam))

print(dir(raw_exam))
