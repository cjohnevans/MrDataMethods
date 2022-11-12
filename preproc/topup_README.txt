# CJE 20220919
# Haven't yet fixed the correct value in datain.txt to scale output fieldmap to Hz
# Also, topup fieldmap may need smoothing

# this uses the standard topup config file
topup --imain=b0_ap_pa.nii --datain=datain.txt --config=b02b0.cnf --out=topup2
# this uses the config file from Greg's pipeline v1.2.8
topup --imain=b0_ap_pa.nii --datain=datain.txt --config=./b02b0_nosubsamp_20220919.cnf --out=topup3
