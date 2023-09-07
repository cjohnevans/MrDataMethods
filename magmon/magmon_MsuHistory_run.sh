#!/bin/bash
source activate mri

last_msu=`find /cubric/scanners/mri/3t-micro/logs -iname 'MsuHistory.log' | sort | tail -n 1`

/home/sapje1/miniconda2/envs/mri/bin/python3 /home/sapje1/code/python_mrobjects/magmon/magmon_MsuHistory.py $last_msu 
cat /home/sapje1/data_sapje1/magmon/connectom/msu_history.csv  |  mailx -s "magmonConnectom" -a /home/sapje1/data_sapje1/magmon/connectom/cryo_temps.png -a /home/sapje1/data_sapje1/magmon/connectom/He_press.png -a /home/sapje1/data_sapje1/magmon/connectom/He_level.png 15f0963a.cf.onmicrosoft.com@uk.teams.ms 
