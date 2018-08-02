# cron_ansible

## Using:

Use vagrant or change ip and user in *ansible/hosts*

Don't forget create and edit *conf.ini* file.

```ini
[email]
from=
address=
password=
smtp=
port=    
```

```bash
chmod +x set_task.py
./set_task.py {start | stop} # !! Stop remove all user cron tasks 
```
