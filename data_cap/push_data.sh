#!/bin/bash

export TheDate=`date`
export Msg="study_bme_1.csv cron pushed csv off the NYC pi at $TheDate"
echo $Msg

#cron runs this periodically
pwd
pushd /home/pi/dev/ZippyMeetsMatplot/data_cap
pwd
git add study_bme_1.csv
git commit -m "$Msg"

#git pull origin master
git push -f origin master    
echo "Pushed!"
popd
pwd