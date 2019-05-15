# Django
Source: https://github.com/pydanny/cookiecutter-django
pipenv shell
pipenv install cookiecutter




cd 01_Django_GITHUB/06_django_vuejs/cookiecutter


cookiecutter https://github.com/pydanny/cookiecutter-django

#Django Vue.js
cookiecutter gh:vchaptsev/cookiecutter-django-vue

cd <project-name>
cd django_vue




## Project creation will cause some odd newlines and linter errors, so I'd recommend:

sudo apt install python-autopep8
autopep8 -r --in-place --aggressive --aggressive .

ERROR: sudo apt install npm
npm run lint --fix



Now you can start project with docker-compose:

docker-compose up --build


For production you'll need to fill out .env file and use docker-compose-prod.yml file:

$ docker-compose -f docker-compose-prod.yml up --build -d