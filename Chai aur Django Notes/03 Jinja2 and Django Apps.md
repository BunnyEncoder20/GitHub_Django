
## Django Apps

- It is important to be on the **root level** where our `manage.py` file is present.
- `manage.py` file is responsible for starting our *Django server* and also making and starting **Django apps**.
- The first step in making these **apps** is the kind of *create* or *make* app command:
```powershell
python manage.py startapp appName
```
- This makes a *new folder* in the name of the **appName** you would've given your app.
- **NOTE** that this command will only *create* the app, but not *install* it in a sense. 
- Basically the Django project doesn't know about the new app yet.
- To make the Main Project about the new app brought in, we will have to modify our main Projects `setting.py` under the : **Application Definations** section. 

```python

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

- Notice how there are already a lot of cooked in (apps made by 3<sup>rd</sup> party people) apps which are already installed by Django.
- Here we just how to add our *app's name*

```python

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'appName',
]
```

- Now our entire Project is aware about the new app (installation in a sense).


### Adding Views, Templates and URLS inside the App

- Consider we made the follow page inside our app's template folder :

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>All Types of Chai</title>
</head>
<body>
    <h1>All Types of Available Tea</h1>
    <hr>
    <ul>
        <li>Masala Chai</li>
        <li>Butter Chai</li>
        <li>Ginger Cardomom Chai</li>
        <li>Tulsi Chai</li>
        <li>Ginger Chai</li>
        <li>Bombay Chai</li>
    </ul>
</body>
</html>
```

- Many people prefer that the Templates and static statics should be kept in the Main projects Template and Static Folders within their own sub folders.
- However many people also prefer that the apps should be developed standalone so that they can be included into any Django project. 
- Hence mostly standard practice is to make the apps own templates, static folders. 
- Also inside the template folder we again create a folder with same name as the app (standard practice) inside which we'll place the templates.
- Hence the views.py *of the app*  will look something like this:

```python
from django.shortcuts import render

# Create your views here.
def all_chai(request):
    return render(request, 'chai/chai_index.html')
```

- But we need to make the **app's url.py file**. 
- We can just copy our main project's url.py file into the app.

- Now we have to pass the control from the **Main Project url.py** to the **App's url.py** for the correct URL resolution.
- For this we need to import the **include** module from **django.urls** package as follows:
```python
from django.urls import include
```
 - hence our **Main Project's** url.py folder would look something like this : 
```python
from django.contrib import admin
from django.urls import path, include

# Importing the views folder
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('info/',views.info,name='info'),

    # This is a redirect to app's url.py
    path('chai/', include('chai.urls')),
]
```
- And our **App's urls.py** would look something like this : 

```python
from django.contrib import admin
from django.urls import path, include

# Importing the views folder
from . import views

# remember these urls are of the form : localhost:8000/chai
urlpatterns = [
    path('',views.all_chai,name='all_home'),
]
```

- **Remember** that the urls coming to the apps's `url.py` file are of the form:
> localhost:8000/appName
- So all the URLs will be of the form : 
> localhost:8000/appName/page1


---

## Jinja2

- The true power of Jinja is it's Templating engine. 
- We will see it's true power in this section.

- Now we want uniformity throughout our app so we want to setup some form of template for all the pages in  our **Main Project** folder level.
- Hence inside the **Main Project's template** folder we add a new file : **layout.html**
- In this we make places for various data by using blocks and variables:

```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>
        {% block title_block %}
            Default Value
        {% endblock %}
    </title>
    <link rel="stylesheet" href="{%style.css%}">
</head>
<body>
    {% block page_heading %}{% endblock %}
    {% block page_body %}{% endblock %}
</body>
</html>
```

- Now this layout document will act as the base on which we can put our dynamic title, heading and content.
- Hence we won't have to rewrite the contents of the layout file every again throughout the project 
- Lets us rewrite our home page to use this layout
	- First we'll have to specify which layout template we want to use at the top using the **extends** injection.
	- And then just remake all the blocks of the **Layout file**. 
	- Our new **index.html** file is reduce to only this : 

```html
 {% extends "layout.html" %}

{% block title_block %}
    Home Page
{% endblock %}

{% block navbar_block %}
    <p>This is where the navbar should be....</p>
{% endblock %}

{% block heading_block %}
    <h1>Welcome User</h1>
{% endblock %}

{% block content_block %}
    <hr>
    <h4>Hellow World !</h4>
    <p>You have reached the Home Page of Bunny's DjangoProject_v0.1 Homepage !</p>
    <br>
    <h5>Powered by Django | Filled in by Jinja | Made by HIM 😎</h5>
{% endblock %}
```

![[Pasted image 20240723183906.png]]
- Now we can replicate this template in all of our webpages, even the ones inside the apps.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>All Types of Chai</title>
</head>
<body>
    <h1>All Types of Available Tea</h1>
    <hr>
    <ul>
        <li>Masala Chai</li>
        <li>Butter Chai</li>
        <li>Ginger Cardomom Chai</li>
        <li>Tulsi Chai</li>
        <li>Ginger Chai</li>
        <li>Bombay Chai</li>
    </ul>
</body>
</html>
```

All of the above can be replaced by the exact same template of our **Main Project's index.html** : 

```html
{% extends "layout.html" %}

{% block title_block %}
    Chai App HomePage
{% endblock %}

{% block navbar_block %}
    <p>This is where the navbar should be....</p>
{% endblock %}

{% block heading_block %}
    <h1>All Types of Available Tea</h1>
{% endblock %}

{% block content_block %}
    <hr>
    <ul>
        <li>Masala Chai</li>
        <li>Butter Chai</li>
        <li>Ginger Cardomom Chai</li>
        <li>Tulsi Chai</li>
        <li>Ginger Chai</li>
        <li>Bombay Chai</li>
    </ul>
    <br>
    <h5 class="footer">Powered by Django | Filled in by Jinja | Made by HIM 😎</h5>
{% endblock %}
```

![[Pasted image 20240723183847.png]]
- Notice how we didn't how to specify Django to look for the layout.html file in the parent folder.
- Djnago by default will search for the specified layout file in the **current app's** template folder, if not there, it'll checkout the **Main Project's** template folder also.
- All this is possible as we have specified in the **setting.py** of the **Main Project Level** that there is templates folder for ever app and is also there in the root level. 


