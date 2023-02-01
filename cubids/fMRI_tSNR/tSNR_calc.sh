#!/bin/bash

fMRIiname=$1
fMRIfname=$2
tSNRoname=$3

echo "Running mcflirt"
mcflirt -in $fMRIiname -out ${fMRIfname}_mc -mats -plots -rmsrel -rmsabs -spline_final

echo "calculating Tmean and Tstd"
fslmaths ${fMRIfname}_mc -Tmean ${fMRIfname}_Tmean
fslmaths ${fMRIfname}_mc -Tstd ${fMRIfname}_Tstd

echo "Performing high pass filter"
fslmaths ${fMRIfname}_mc -bptf 50 -1 -add ${fMRIfname}_Tmean ${fMRIfname}_mc_tempfilt
# 100s cut-off high-pass temporal filter (mean added back in)

echo "Performing brain extraction"
bet ${fMRIfname}_Tmean ${fMRIfname}_brain -m -Z -f 0.2

echo "Calculating tSNR"
fslmaths ${fMRIfname}_Tmean -div ${fMRIfname}_Tstd ${fMRIfname}_tSNR

echo "Calculating mean value within masked region"
fslstats ${fMRIfname}_tSNR -k ${fMRIfname}_brain_mask -M >> $tSNRoname
# Standard out gives mean tSNR over a loose brain mask
