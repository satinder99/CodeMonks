# CodeMonks

## How to use this app
> ## Setup database
> 1. Install mysql database (preferably).
> 2. Create a user with access to a database to let django communicate with the DB

> ## Clone the repo
> 1. Use git clone for the desired branch
> 2. Activate virtual environment using python's (Version 3.7) virtualenv module

> ## Setup the environment
> 1. Open the settings.py file and edit the appropriate parameters of DATABASES dictionary
> 2. install the modules from requirements.txt file.
> ```python
> pip install -r requirements.txt
>```

> ## Start the development server
> 1. First migrate some essential models.
> ```python
> python manage.py makemigrations
> python manage.py migrate
>```
> 2. Start the development server
>```python
> python manage.py runserver
>```
> 3. If it works well, host the app using a dedicated server.