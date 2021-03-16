# INSTRUCTION

1. sudo -H pip install -U pipenv -> install right pipenv

## LIBRERIA

1. pipenv shell
2. pipenv install colorama
3. pipenv lock -r -> detalles
4. pipenv graph -> list package
5. pipenv uninstall colorama -> desinstalar
6. pipenv install colorama --dev -> solo para desarrollo
7. pipenv check -> para verificar las seguridad de los package
8. pipenv install -> update packages

## FRAMEWORKS

-> Create file requirements.txt
-> Write in requirements => Django==2.1.2
-> pipenv install -r requirements.txt

## DJANGO RUN

-> django-admin startproject hello
-> cd hello
-> python manage.py runserver

## DEPLOYMENT

1. pipenv lock
2. pipenv install --ignore-pipfile -> instalar con todas sus versiones ignorando el archivo pipfile
3. exit -> para salir del entorno virtual
4. pipenv --rm -> removido el entorno virtual
5. pipenv shell -> inicia nuevo entorno virtual, sin dependecias
6. pipenv install -> para instalar las dependecias
7. pipenv install --dev -> para instalar las dev dependecias
