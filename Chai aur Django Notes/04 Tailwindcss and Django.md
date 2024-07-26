- Normally, it is difficult to make traditional Tailwind to work inside of Django
- Hence there is a separate package made for it : **django-tailwind**.
- We can install it into our venv using the following command : 
```powershell
uv pip install django-tailwaind
```
- But we would like the sites to hot loaded also when we are making changes in the code so we can include that in the same installation command : 
```cmd
uv pip intall 'django-tailwind[reload]'
```

> Ensure that the output of the command looks like **this**.
![[Pasted image 20240724184839.png]]
- This is important as we do not want **uv** to *audit* the package instead. In that case we will have to install pip into our `.venv ` and use that directly to install the above command.
- More info in this [blog article](![[Pasted image 20240724185726.png]]).

##### Once **django-tailwind** is installed, We have to follow the below instructions *in order* :

> 1. In our **Main Project's** `settings.py` file we have to add **tailwind** app in the *INSTALLED_APPS* section:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'chai',
    'tailwind',
]
```

2. Go to the **Terminal** and enter in the command : 

```
python manage.py tailwind init
```
- This will generate the necessary tailwindcss files for our project.
- **Note :** if you have used **uv** till here and used it to make the venv, chances are that it might not be working well. If the **django-tailwind** package installation is causing errors like "Module Not Found", then try reinstalling the .venv : 

```
deactivate

rm -r .venv

python -m venv .venv

.venv\Scripts\activate
```

- after the reinstallation, again try the django-tailwind init command, it'll work as expected.

- At the end of the init command, we can choose our app name, press enter to leave it at default (**theme**).

 3. Adding **"theme"** app in the **INSTALLED_APPS** list
- The above action will create a folder named **theme** at our **Main Project** (root) folder level. As this is a new *app*, we'll have to add this to our list of **INSTALLED_APPS** in the `settings.py` file : 
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'chai',
    'tailwind',
    'theme',
]
```

4. Adding Important Configurations : 
- Next in the same `settings.py` file we will add our *tailwindcss app* name : 

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'chai',
    'tailwind',
    'theme',
]

TAILWIND_APP_NAME = 'theme'
```

5. Defining the **internal IP** & Adding **NPM_BIN_PATH**
- set the *internal IP* of this server (cause we gonna run multiple in some time)
- Also specify the **nodeJS and npm bin path** as shown
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'chai',
    'tailwind',
    'theme',
]

TAILWIND_APP_NAME = 'theme'
INTERNAL_IPS = ['127.0.0.1']
NPM_BIN_PATH = "C:/Program Files/nodejs/npm.cmd"
```

7. Now Install **tailwind** 
- Finally install tailwind into the Django project using the `manage.py` file:
```
python manage.py tailwind install
```

---

### Adding Tailwind into Pages

- Now we can add tailwind anywhere in the project using the below 2 lines : 
```djnago-html
{% load static tailwind_tags %} %% Top of the page %%

{% tailwind_css %}              %% Inside the head tag %%
```

But first we must start the tailwind generation in another using the command  ;

```
python manage.py tailwind start
```

Then we will start our djnago project server in another terminal: 

```
python manage.py runserver
```

- At the end of the proejct when everything is done, we can simply run the command : 
```
python manage.py tailwind build
```
- To get the finalized version

**BUT** as you might have noticed, our hot reloading is not working. Time to make that accessible
- First we need to add it's *app name* in the **INSTALLED_APPS** section of the `settings.py` of the main folder.
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'chai',
    'tailwind',
    'theme',
    'django_browser_reload',
]
```
- and also add it's corresponding **MIDDLEWARE**:

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django_browser_reload.middleware.BrowserReloadMiddleware',
]
```

- Finally we need to go into **Main Projects** and add the hot reload link (**NOTE** this url should *always be the last one*)
- Restart both the terminal servers to see the hot reloading.

---

## Django's Admin Panel

#### Enable the admin panel in Django

- All settings and urls for the admin panel are already provided in django.
- First run the **migrate command** to create the necessary tables for the admin panel:
```
python manage.py migrate
```
- Next is to create the **admin user**:
```
python manage.py createsuperuser
```
- Add your username, email (this can be empty), and password to the `createsuperuser` command.
> username : bunny
> password : somasenpai2020#

- Now we can login into the admin panel by going to : http://127.0.0.1:8000/admin (the routes are already made in our `urls.py` files)

---


