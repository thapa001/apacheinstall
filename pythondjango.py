#!/usr/bin/python
import os #import os library
#define setup_install function
def setup_install():
        print(" Installing stuff")
        os.system('yum -y install python-pip') #install python
        os.system('pip install virtualenv') #pip is python command
        os.system('pip install --upgrade pip') #upgrade
        os.mkdir('/opt/django') #make folder
        os.chdir('/opt/django') #change to folder
        os.system('yum -y install python36') #install python3.6
        os.system('virtualenv -p python36 django') #download the django environment
        os.system('python --version')   #check python version
        # activate and install django and start project- all this must be on one line
        # version check not necessary
        os.system('source /opt/django/django/bin/activate && pip install django' + \
                                '&& django-admin --version'  + \
                                '&& django-admin startproject project1')
        os.system('chown -R pradip00700pradip /opt/django') #change owner
        
#start django function          
def django_start():
        print('starting django')
        #start django project
        os.system('sudo -u pradip00700pradip sh -c "source /opt/django/django/bin/activate' + \
                   ' && python /opt/django/project1/manage.py runserver 0.0.0.0:8000&"')
                   
#call functions
setup_install()
django_start()
