# https://docs.graphene-python.org/projects/django/en/latest/installation/

# https://www.section.io/engineering-education/integrating-graphql-api-in-a-django-application/

# https://www.twilio.com/blog/graphql-apis-django-graphene

mkdir django_graphql
cd django_graphql
/home/shoumitro/.pyenv/versions/3.6.12/bin/python -m venv env
source ./env/bin/activate
pip install django graphene-django
django-admin startproject books_api
cd books_api
python manage.py startapp api
python manage.py makemigrations
python manage.py migrate

# load json data into sqlite3
python manage.py loaddata data.json

# Introspection Schema 
python manage.py graphql_schema
python manage.py graphql_schema --schema api.schema.schema --out schema.json

python manage.py runserver 127.0.0.1:7000
http://127.0.0.1:7000/graphql



USER: shoumitro
PW: QWERTYU12345678


 # data.json
 
 [
    {
        "model": "api.book",
        "pk": 1,
        "fields": {
            "title": "The One Thing",
            "author": "",
            "year_published": 2002,
            "review": 3
        }
    },

    {
        "model": "api.book",
        "pk": 2,
        "fields": {
            "title": "Python Crash Course",
            "author": "Eric Matthes",
            "year_published": 2015,
            "review": 5
        }
    },

    {
        "model": "api.book",
        "pk": 3,
        "fields": {
            "title": "Atomic Habits",
            "author": "James Clear",
            "year_published": 2002,
            "review": 4
        }
    },

    {
        "model": "api.book",
        "pk": 4,
        "fields": {
            "title": "The Compound Effect",
            "author": "Darren Hardy",
            "year_published": 2010,
            "review": 3
        }
    },

    {
        "model": "api.book",
        "pk": 5,
        "fields": {
            "title": "Clean Code",
            "author": "Robert Cecil Martin",
            "year_published": 2008,
            "review": 4
        }
    }
]
