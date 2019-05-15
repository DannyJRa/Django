# Administration of 03_SB_Admin_Bootstrap_4

## Activate pipenv
pipenv shell

pipenv install -r requirements.txt

## Start by choosing the settings set-up
cd src
cd testproj
python manage.py migrate
python manage.py runserver 0.0.0.0:8001



### Test3
git clone https://github.com/axnsan12/drf-yasg.git
cd drf-yasg
virtualenv venv
source venv/bin/activate


cd testproj
python -m pip install -U pip setuptools
pip install -U -r requirements.txt
python manage.py migrate

#Change host
settings/base.py
35.207.187.143

RUN
python manage.py runserver 0.0.0.0:8001