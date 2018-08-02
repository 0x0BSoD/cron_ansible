#!/usr/bin/env python

import getpass
import os
import sys
from crontab import CronTab

cron = CronTab(user=getpass.getuser())

job = cron.new(command='python ' + os.path.abspath('runner.py'))

try:
    action = sys.argv[1]
    if action == "start":
        job.minute.every(10)
    elif action == "stop":
        cron.remove_all()
    else:
        print("? exiting...")
        sys.exit(1)
except IndexError:
    print("Need argument start/stop exiting...")
    sys.exit(1)

for item in cron:
    print(item)

cron.write()