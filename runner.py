#!/usr/bin/env python

from subprocess import Popen, PIPE
import configparser
import shlex

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

cfg = configparser.ConfigParser()
cfg.read('conf.ini')
e_cfg = cfg['email']

def send_mail(address, result, last_ten=None):
    
    if result:
        body = "Running Succes"
    else:
        body = "Running Fails \n {}".format(last_ten)

    fromaddr = e_cfg['from']

    toaddr = address
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Ansible Cron run result"

    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP(e_cfg["smtp"], str(e_cfg["port"]))
    server.starttls()
    server.login(fromaddr, e_cfg["password"])
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

def run_task(notify=False):

    cmd = "ansible-playbook -i ansible/hosts ansible/init.yml"
    p = Popen(shlex.split(cmd), stdout=PIPE, stderr=PIPE)
    out, err = p.communicate()
    p.wait()
    rc = p.returncode
    if rc == 0:
        print("="*15)
        print("DONE!")
        print("="*15)

        result = True
    else:
        print("="*15)
        print("ERROR!")
        print("="*15)

        result = False

    if notify: 
        send_mail(e_cfg["address"], result, out.decode())

if __name__ == "__main__":
    run_task(notify=True)
