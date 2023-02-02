#!/bin/bash
singularity run -B /cubric:/cubric  /cubric/software/cubids/containers/python/pc.sif python3 /cubric/software/cubids/core/fsl/fMRI_tSNR/tSNR_basic.py $1
