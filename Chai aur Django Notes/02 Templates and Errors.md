## Django Web Workflow

- Django is a Framework
- Every Framework works on a underlying tech stack.
- The flow of Django is as follows (When a request comes to it):

1. User sends a request to the website.
2. Website sends the request to Django.
3. Django sends the request to the URL resolver
4. URL resolver further sends it to the `urls.py` files (can be multiple of them)
5. The `url.py` path will send to fetch a `views.py` file. The `views.py` file is the **main controller** where all the actual logic resides.
6. If there is a DB involved in the `views.py` file, it will send request to `models.py` file. `models.py` file will in turn ping the DB.
7. After this, the `views.py` will send the response back to the website.
8. Sometimes the response can also be sent via the `template.py` file.

- The basic workflow of Django can be summarized as follows:
```
user -> request -> url.py -> views.py -> response -> user
```
![Django Program Flow](image001.png)

---

## Creating a Views file

- Create a file named `views.py` at the **Project level** (note that means inside the inner folder with the same name as the Project)

> **NOTE** that the name of the file **MUST** be `views.py` only. This is the rules of the framework and naming it anything else can cause issues.

- Let us make a simple `views.py` file for explanation.

```python 
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, world. You're at the DjangoProject01 home page.")

def about(request):
    return HttpResponse("Hello, world. You're at the DjangoProject01 about page.")

def contact(request):
    return HttpResponse("Hello, world. You're at the DjangoProject01 contact page.")
```

---

## Creating the URLs file

- We import the views file into the `urls.py` file so that we can reference it's functions 
- The home route is given by: `path('', views.home, name='home')` (notice the empty ' ')
- The slashes at the end of `path` are necessary.
- Don't forget the commas at the end of the paths function.

```python 
from django.contrib import admin
from django.urls import path
from . import views             # importing the views file to access it's functions

urlpatterns = [
    path('admin/', admin.site.urls),                    # admin route
    path('', views.home, name='home'),                  # home route
    path('about/', views.about, name='about')           # about route
    path('contact/', views.contact, name='contact'),    # contact route
]
```

---

## Loading Templates Files 

- On the **root level** we also create the `templates` and `static` folders.
- Within the **static** folder, we will put the `css` and `js` files for the website
- Within the **templates** folder, we will put the `html` files
- Consider the following html file in **template folder**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Django Project</title>
</head>
<body>
    <h1>Chai aur Django</h1>
</body>
</html>
```
- In order to show this "Template" page on the website when we go to the url, we must modify the response we give in the **`views.py`** file
- This is called **rendering** a template (sending a template html file as a response). 
- the **`render(request, 'template_name.html')`** function is import from `django.shortcuts` (`django.shortcuts` is a very powerful library and we will be using it a lot further)

```python
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello, world. You're at the DjangoProject01 home page.")
    return render(request, 'index.html')
```
- If the template file which we want is within another folder, then we need to specify that in the **`render(request, 'folder_name/template_name.html')`** function.

```python
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'website/index.html')
```

<br>

- However, we cannot directly load the templates even though we have specified it in the `views.py` file. 
- We need to config the **`settings.py`** file to tell the project from where to load the templates from:
- Within the **`TEMPLATES`** section we can see the config for the templates. 
- In the **'DIRS'** list we can mention the folder name from where we want to fetch the template files from.

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
- Now the template page will load correctly.

---

## Loading static files

- The same way we created the html files within the template folder, we can make the static files like `style.css` and `index.js` within the **`static folder`**.
- **`static folder`** is present at the root level, same as the template folder.
- Consider the following css code in a style.css within the **`static folder`**:

```css
body{
    background-color: rgb(0, 72, 97);
    color: white;
}

h1{
    text-align: center;
    font-size: 5em;
}
```
- Now, we cannot directly link up the html and the css file using the traditional `<link>` attribute.
- Eg: The following will not be able to load the css properties.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Django Project</title>
    <link rel="stylesheet" href="../static/style.css">  <!-- Doesn't work -->
</head>
<body>
    <h1>Chai aur Django</h1>
</body>
</html>
```

- We need to incorporated the **Templating Engine** of Django.
- In basic terms, it's a means to inject code into any part of the project. (Similar to the way we injected php code into our JS files).
- In Django, we use the **`{% %}`** to inject the code.
- Eg:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Django Project</title>
    <link rel="stylesheet" href="{% static 'style.css' %}">  <!-- Doesn't work -->
</head>
<body>
    <h1>Chai aur Django</h1>
</body>
</html>
```
- The `static` keyword signifies that the injection is *loading a static asset*. 
- Then we have given the file *name of the static asset* to be loaded.
- But You will still get the following error message:

```
TemplateSyntaxError at /

Invalid block tag on line 7: 'static'. Did you forget to register or load this tag?

Request Method: 	GET
Request URL: 	http://127.0.0.1:8000/
Django Version: 	5.0.6
Exception Type: 	TemplateSyntaxError
Exception Value: 	

Invalid block tag on line 7: 'static'. Did you forget to register or load this tag?

Exception Location: 	C:\Users\gener\Coding\GitHub-Django\.venv\Lib\site-packages\django\template\base.py, line 565, in invalid_block_tag
Raised during: 	DjangoProject01.views.home
Python Executable: 	C:\Users\gener\Coding\GitHub-Django\.venv\Scripts\python.exe
Python Version: 	3.11.7
Python Path: 	

['C:\\Users\\gener\\Coding\\GitHub-Django\\DjangoProject01',
 'C:\\Users\\gener\\AppData\\Local\\Programs\\Python\\Python311\\python311.zip',
 'C:\\Users\\gener\\AppData\\Local\\Programs\\Python\\Python311\\DLLs',
 'C:\\Users\\gener\\AppData\\Local\\Programs\\Python\\Python311\\Lib',
 'C:\\Users\\gener\\AppData\\Local\\Programs\\Python\\Python311',
 'C:\\Users\\gener\\Coding\\GitHub-Django\\.venv',
 'C:\\Users\\gener\\Coding\\GitHub-Django\\.venv\\Lib\\site-packages']

Server time: 	Mon, 20 May 2024 13:13:18 +0000
```

- In order to resolve this we must **tell the template to load static assets**.
- As we are going to use them in the template. This is done by adding a similar injection at the top of our *index.html* template file:

```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Django Project</title>
    <link rel="stylesheet" href="{% static 'style.css' %}">  <!-- Doesn't work -->
</head>
<body>
    <h1>Chai aur Django</h1>
</body>
</html>
```

- Now, the error will be gone, but the css properties are still not loading. 
- This is due to the path  `/static/style.css` not being available. To fix this, we again go to the **`settings.py`**
- The **`settings.py`** file contains the default path for a static asset to load from. 
- But we also need to make a static dirs which will tell the project where our static assets are kept and to load them using their full path. (We import the package **`os`** for this.)
- Eg: 

```python
from pathlib import Path
import os

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
```

- The static dir is supposed to be located right below the 
> STATIC_URL = 'static/' 
- This is production practice and that is where we will always write it. 
- As everyone will expect those settings to be at that place.



