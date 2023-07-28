# Pre-checklist install
Creating The environment

`!Only needs to be done once!`

```console
    Windows- (command prompt): | python -m venv djangoPy3Env
```
Activating the environment

```console
    Windows- (command prompt): | call djangoPy3Env\Scripts\activate       
    Windows- (git bash):| source djangoPy3Env/Scripts/activate
```
Install Django:
```console
(djangoPy3Env) Windows/Mac: | pip install Django
```


# Start of checklist
- Create a folder for new project
    - go into that folder
- create a new django project

`! Inside the project folder run this command !`
```console
    django-admin startproject project_name
```
- A new project (project_name) has been created
- run the project using:
```console
    python manage.py runserver
```
- Open localhost:8000
    - ctrl-c to stop the server

- For every app we want to add to our project

```console
project_name > python manage.py startapp app_name
```

- Go to settings.py under the folder with the same name as the project. Find the variable INSTALLED_APPS,
    - Add our newly created app

```py
INSTALLED_APPS = [
    'app_name', # added this line. Don't forget the comma!!
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]    # the trailing comma after the last item in a list, tuple, or dictionary is commonly accepted in Python
```

- Go to urls.py and add a URL pattern for your new app. 
    - You will need to add an import for your views file.

```py

from django.urls import path, include # import include
# from django.contrib import admin    # comment out, or just delete

urlpatterns = [
    path('', include('your_app_name_here.urls')),	   
    # path('admin/', admin.sites.urls)         # comment out, or just delete
]
```

- Create a new urls.py file in app_name folder.
    -   Put the following code
```py
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
]
```
- Put a function called index in app's views.py file
```py
from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
def index(request):
    return HttpResponse("this is the equivalent of @app.route('/')!")

```

- Run the app again using
```console
python manage.py runserver
```
<style> 
.test{
    color: red
}
</style>
<p class="test">
# Do not manually change the name of folders after creation </p>

- after this run this command to dismiss unapplied migrations as well as have session available 

    - do it inside the project

```console
project_name> python manage.py migrate
```