# Portfolio-Website
Django based portfolio website 

Create 2 folders inside src folder, named media and static. 

You can install the project in 2 ways - with adn withough virtual environment (I would recommend using virtual environment to separate your dependencies). 

This assumes that you're using Ubuntu Linux for the installation:

    Installing the Python tools needed for the enviroment

Open up the Terminal Application and start typing the following:
```

$ sudo apt-get install python-pip python-virtualenv python-setuptools python-dev build-essential python3.6
```


    Installing the virtual enviroment
    
```
$ sudo pip install virtualenv
```

    Making the directories for the project
    
```
$ mkdir ~/Dev

$ cd ~/Dev

$ mkdir venv && cd venv

$ virtualenv -p python3.6 .
```

    Now we test if Virtual Enviroment has been installed

```
$ cd ~/Dev/venv/

$ source bin/activate
```

Once you activate the virtual environment you can start installing the dependencies: 
```
pip3 install django==3.0.3 
pip3 install django-mathfilters 
pip3 install django Pillow
```

Finally, go into the directory where the file "manage.py" is and run the following in the terminal: 
```python3 manage.py makemigrations 
python3 manage.py migrate
```

To start the project run: 
```python3 manage.py runserver```

There is already a superuser created which will allow you to access the /admin: username: user password: user
