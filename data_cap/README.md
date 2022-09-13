# cron setup for Bosch BME sensor data commit
## 
### This would run the script at minute 0 and hour 0 of every day of every month (midnight, daily) 
```bash
0 0 * * * /home/pi/dev/ZippyMeetsMatplot/data_cap/push_data.sh > /home/pi/dev/ZippyMeetsMatplot/data_cap/cron_run.log 2>&1
```

sample output of the cron job logs to `cron_run.log` includes both stdout and stderr 

```bash
study_bme_1.csv cron pushed csv off the NYC pi at Tue 14 Jun 2022 09:30:01 PM EDT
/home/pi
~/dev/ZippyMeetsMatplot/data_cap ~
/home/pi/dev/ZippyMeetsMatplot/data_cap
[master 2cda242] study_bme_1.csv cron pushed csv off the NYC pi at Tue 14 Jun 2022 09:30:01 PM EDT
 1 file changed, 5 insertions(+)
To github.com:dfinke/ZippyMeetsMatplot.git
 + bc6627a...2cda242 master -> master (forced update)
Pushed!
~
/home/pi
```

## Column headers for study_bme_1.csv are:

```Python
header=["humidity","temp","gas","pressure","timestamp"]
```


