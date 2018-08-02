#!/usr/bin/env python

import getpass
import os
import sys

from crontab import CronTab


cron = CronTab(user=getpass.getuser())

w_dir = os.path.dirname(os.path.realpath(__file__))
runner = os.path.abspath('runner.py')
job = cron.new(
    command='PATH=/usr/local/bin:/usr/local/sbin:~/bin:/usr/bin:/bin:/usr/sbin:/sbin; env; cd {}; python {}'.format(w_dir, runner))

try:
    action = sys.argv[1]
    if action == "start":
        job.minute.every(1)
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
