python -m venv env    
.\env\Scripts\activate 
pip install django djangorestframework django-cors-headers
python manage.py runserver
Run the database migrations:

sh
Copy code
python manage.py makemigrations
python manage.py migrate

POST 

{
    "city": "New York",
    "temperature": "25°C"
}

Search

http://127.0.0.1:8000/weather/search_param/?city=london

