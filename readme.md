## Create Virtual env

python -m venv env    

.\env\Scripts\activate 

## install django 

pip install django djangorestframework django-cors-headers

python manage.py runserver

## Run the database migrations:

python manage.py makemigrations
python manage.py migrate



