#!/bin/bash

export TheDate=`date`
export Msg="cron pushed csvs off the NYC pi at $TheDate"
echo $Msg

#cron runs this periodically
pwd
pushd /home/pi/dev/dash_weather/data_cap
pwd
git add basement_bme688.csv
git commit -m "$Msg"

#git pull origin master
git push -f origin master    
echo "Pushed!"
popd
pwd
