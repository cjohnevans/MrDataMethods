#!/bin/bash
echo dicom_mb_check INPUT_DICOM

dcm_file=$1

/cubric/software/afni/dicom_hdr -sexinfo $dcm_file  > dcm.hdr
echo '>>> SEQUENCE >>>'
grep tSequenceFileName dcm.hdr 
echo '>>> MULTIBAND-FACTOR >>>'
grep 'adFree\[4\]' dcm.hdr
grep 'alFree\[13\]' dcm.hdr

rm dcm.hdr
