Quickstart: https://vsupalov.com/cookiecutter-django-quickstart/

pipenv install -r requirements/local.txt

pipenv shell




export DATABASE_URL="sqlite:///db.sqlite"



python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 0.0.0.0:8001



create a bash script with the following:

#!/bin/bash
exec ./manage.py runserver 0.0.0.0:8001
save it as runserver in the same dir as manage.py

chmod +x runserver
and run it as

./runserver