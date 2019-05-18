# Django
Source: https://github.com/pydanny/cookiecutter-django
pipenv shell

pipenv install cookiecutter




cd 01_Django_GITHUB/06_django_vuejs/cookiecutter


cookiecutter https://github.com/pydanny/cookiecutter-django

#Django Vue.js
cookiecutter gh:vchaptsev/cookiecutter-django-vue

cd <project-name>
cd 01_Dango_GITHUB/06_django_vue/django_vue




## Project creation will cause some odd newlines and linter errors, so I'd recommend:

sudo apt install python-autopep8
autopep8 -r --in-place --aggressive --aggressive .

ERROR: sudo apt install npm
npm run lint --fix



Now you can start project with docker-compose:

docker-compose up --build


For production you'll need to fill out .env file and use docker-compose-prod.yml file:

$ docker-compose -f docker-compose-prod.yml up --build -d


## Docker bash

sudo docker exec -it  django_vue_graphql_backend_1 bash


python manage.py createsuperuser




## Postgresql

Docker volumes:

volumes:
    postgres_data: {}

Means it create docker volumens

volumes:
 mysql:
You can list the docker volumes using docker volume ls and the 'path' will be something like: /var/lib/docker/volumes/mysql/date. When you cd in this folder you will see the same data as the data which is in your mysql container on path: /var/lib/mysql. If you exec inside your container you will see the same data.

cd /var/lib/docker/volumes/django_vue_postgres_data