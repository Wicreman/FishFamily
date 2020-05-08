1. install community mysql installer
https://dev.mysql.com/downloads/installer/

2. install mysql  
3. set password of user "root" as root
4. run bootstrap.ps1
5. replace "H:" with your enlistment drive
file: H:\FishFamily\fishs\utility\syncbuild.cmd
H:\FishFamily\fishs\apps\bluefish\views.py
6. config your allowed IP: 
ALLOWED_HOSTS = ['x.x.x.x']
H:\FishFamily\fishs\bluefish\settings.py
7. run python manage.py runserver 0.0.0.0:8000
