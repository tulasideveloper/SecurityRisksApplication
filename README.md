# SecurityRisksApplication
Pre requisites: On Windows 10 Python 3.8

# Step 1: 
# Create a virtual environment on the project folder

->Open  Command prompt and root to the downloaded project directory

$ pip install virtualenv

# Activate Virtualenv

$ .\Scripts\Activate

# Step 2:

## Install Django framework
$ pip install Django==3.0.1

## Django Forms Template Library
$ pip install django-crispy-forms==1.9.0

## PostgreSQL command line
$ pip install psycopg2==2.8.4

## Install PostgreSQL GUI version

https://www.postgresql.org/download/windows/

# Step 3:

->  Root to Project Directory BusinessLogic

-> $ python manage.py makemigrations

-> $ python manage.py migrate

-> $ python manage.py runserver

-> Open browser and copy the address  localhost:8000






