#!/bin/bash
# check that the 7T logs have been updated - send an error to the teams channel if there 
# hasn't been an update in the past day.


lastday=`find /cubric/scanners/mri/7t/magnet_logs -mtime -1 -iname '*magmon*'`
lastlog=`ls -1rt /cubric/scanners/mri/7t/magnet_logs/magmon* | tail -n 1`

if [ -z $lastday ]
then
    echo "No magmon data from 7T past 24 hours.  Last log file = "$lastlog | mailx -s "magmon7T Warning" 15f0963a.cf.onmicrosoft.com@uk.teams.ms 
fi
