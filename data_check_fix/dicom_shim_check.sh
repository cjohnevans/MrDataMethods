#!/bin/bash

dcm_file=$1
tmp_file=`mktemp /tmp/tmp_dcm.XXXXXXXX`

/cubric/software/afni/dicom_hdr -sexinfo $dcm_file > $tmp_file

# scan header info
uid=`cat $tmp_file | grep 'PAT Patient ID' | awk -F// '{print $3}'`
series=`cat $tmp_file | grep 'REL Series Number'| awk -F// '{print $3}'`
desc=`cat $tmp_file | grep 'ID Series Description'| awk -F// '{print $3}'`
# shim header info
x=`cat $tmp_file | grep 'lOffsetX' | awk -F= '{print $2}'`
y=`cat $tmp_file | grep 'lOffsetY' | awk -F= '{print $2}'`
z=`cat $tmp_file | grep 'lOffsetZ' | awk -F= '{print $2}'`
a20=`cat $tmp_file | grep 'ShimCurrent\[0' | awk -F= '{print $2}'`
a21=`cat $tmp_file | grep 'ShimCurrent\[1' | awk -F= '{print $2}'`
b21=`cat $tmp_file | grep 'ShimCurrent\[2' | awk -F= '{print $2}'`
a22=`cat $tmp_file | grep 'ShimCurrent\[3' | awk -F= '{print $2}'`
b22=`cat $tmp_file | grep 'ShimCurrent\[4' | awk -F= '{print $2}'`

#echo x,y,z,A20,A21,B21,A22,B22,uid,series,protocol
echo $x,$y,$z,$a20,$a21,$b21,$a22,$b22,$uid,$series,$desc
