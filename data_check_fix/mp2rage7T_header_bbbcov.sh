#!/bin/bash
# mp2rage7T_header_bbbcov INPUTDCM.dcm
#   change the header info from a retro recon 7T MP2RAGE to put the participant and
#   study info in the correct fields for BBBCOV project
#   uses;
#     /cubric/software/afni/dicom_hdr 
#     /cubric/software/dcmtk/bin/dcmodify
#   cje June 2022, updated for bbbcov in March 2023


dcmfile=$1

echo "Before...."
echo $dcmfile
dicom_hdr $dcmfile | grep '0010 0010'   # patient id
dicom_hdr $dcmfile | grep '0010 0020'   # 'patient id' = session id.
# these two are fixed across the project
dicom_hdr $dcmfile | grep '0040 0254'   # protocol folder
dicom_hdr $dcmfile | grep '0008 1030'   # project id
dicom_hdr $dcmfile | grep '0020 0011'   # series no

ismag=`dicom_hdr $dcmfile | grep "_MAG$"`

# set the series no. for each to be 300 or 301 to avoid clashes
if [ "${#ismag}" -gt 0 ];  # if ismag length is non-zero
then
   echo "it's magnitude"
   series_no=300
else
   echo "it's phase"
   series_no=301	
fi

# grab ppt_id, session_id
# search for the beginning of the ppt ID, a start of line
# sed to alter default formatting of  scan UID to match XNAT
ppt_id=`dicom_hdr ${dcmfile} | grep ^CAU| sed s/'\.'/_/g | sed s/:/_/g | awk -F/ '{print $1}'`
sess_id=`dicom_hdr ${dcmfile} | grep ^CAU | sed s/'\.'/_/g | sed s/:/_/g | awk -F/ '{print $3}'`

#ppt_id
dcmodify -m 0010,0010=${ppt_id} ${dcmfile}
dcmodify -m 0010,0020=${sess_id} ${dcmfile}
dcmodify -m 0008,1030='476_bbbcov' ${dcmfile}
dcmodify -m 0020,0011=${series_no} ${dcmfile}

echo "After..."
dicom_hdr $dcmfile | grep '0010 0010'   # patient id
#dicom_hdr $dcmfile | grep '0040 0254'   # protocol folder
dicom_hdr $dcmfile | grep '0008 1030'   # project id
dicom_hdr $dcmfile | grep '0010 0020'   # 'patient id' = session id.
dicom_hdr $dcmfile | grep '0020 0011'   # series no

