# Administration of 03_SB_Admin_Bootstrap_4

## Give user access to folder

sudo chown -R danny $HOME/OneDrive/DataScience/02_CloudComputing/16_Django/


## Activate pipenv
pipenv shell

## Start by choosing the settings set-up
cd 01_Django_GITHUB/03_SB_Admin_Bootstrap_4/django
python manage.py runserver --settings=admin_proj.settings.cloud

python manage.py runserver --settings=admin_proj.settings.settings_local

python manage.py runserver 0.0.0.0:8001 --settings=admin_proj.settings.settings_local


python manage.py runserver 0.0.0.0:8001 --settings=admin_proj.settings.cloud
## Go to site
http://localhost:8000/admin_app/


## Migrate
python manage.py migrate --settings=admin_proj.settings.cloud


# Vue.js In A Django Template
Source: https://vsupalov.com/vue-js-in-django-template/
## Create app

python manage.py startapp simple_vuejs
