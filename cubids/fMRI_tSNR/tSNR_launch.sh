#!/bin/bash
singularity run -B /cubric:/cubric  /cubric/software/cubids/containers/python/pc.sif python3 /home/sapje1/code/python_mrobjects/cubids/fMRI_tSNR/tSNR_basic.py $1
