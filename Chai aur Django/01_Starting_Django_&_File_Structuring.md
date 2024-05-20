# Starting with Django Project and File Structuring

---

- Documentation : [Django Docs]('https://docs.djangoproject.com/en/5.0/')
- Django is a old framework, which means it very fast and requires lesser resources to run 
- In production level development, Django or Python code is usually written in a virtual environment instance. (cause everyone might not have the same packages and versions installed)
- In this separate instance or Sandbox env, we can write our code and what is installed in our main system will not effect it at all.

---
---

## Setting Up Django in a Venv

### Virtual Environment Creation 

```
py -m venv .venv
```
- This is the **traditional way** the virtual environments were created in python.
> **py** = python3
> **-m** = module
> **venv** = command to make a virtual environment
> **.venv** = name of the hidden folder in which the files related to the virtual environment will be stored

- The newer (better and faster) way of creating virtual environments and managing packages of python is by using [UV package]('https://pypi.org/project/uv/').
- **uv** An extremely fast Python package installer and resolver, written in Rust.
- Can be installed using : 

```python
pip install uv
```
- To create a virtual environment using **uv** use the command: 
```
uv venv  # creates a virtual environment at .venv
```
- This only installs the virtual environment. 
- Next we have to activate the virtual environment:
```
.venv\Scripts\activate
```
- After activating the virtual environment, we can install whatever packages using pip.
- To deactivate the virtual environment:
```
deactivate
```

---

### Installing Packages in Virtual Environment

- we can use the following command to install packages in our virtual environment:
- Note that we need to be inside the venv (the virtual env must be activated) for these to happen. (Obviously 🙄)
```
uv pip install packageName
```

---

### Installing Django in the venv

- we can install Django into our newly craeted venv using the following command: 
```
uv pip install Django
```
---

### Creating Django Project in Virtual Env

- When we create a project of Django for the first time there can be a little confusing. 
- one of the main commands is:
```
(.venv) django-admin
```
- This is called a main command.
- We then add some sub commands to this 
- Eg: when we are initializing a Django project for the first time, we use the "project" command:
```
(.venv) django-admin startproject projectName
```
- **NOTE:** That we must have the Project folder as the same File dir as the .venv folder.
- There **should** be another folder within the Project master folder with the same name.
- This is standard practice 
  
<br>

- Next we need to navigate into the Folder and run the Django server:

```
> cd .\projectName
> python .\manage.py runserver 
```
- By default the Django will run on the port `8000`
- but we can make it run on a desrired port by adding the port number at the end of the command:

```
> python .\manage.py runserver 8001
```
- To stop the server use: `ctrl+C`
---

## File System Exploration 

### manage File

- **`manage.py`** is the main starting point file of a Django Project.
- This sets many things like venv variables
- This is also the file which invokes the entire project (runs first and starts the project) in production.

<br>

- It is important that we know what the levels of the Project folder are as we need to place other important folders in prefect hierarchy.

>- First Level is the **Project Main Folder** which is called the **Root Level** 
>- The the folder with the same name is called the **Inside Folder Level** or **Project Level**
>- The Level at which **`manage.py`** is kept is called the **root level**
>- There is also a **app level**

<br>

- Notice that we also got a **`db.sqlite3`** file also. 
- sqlite3 is the default data base which is used in Django
- With some Minor configuration settings, we can easily convert the DB into `MySQL` or `PostGress`.

<br>

- In the **Project Level** there is the **`__pycache__`** folder which is responsible for the caching of the files when multiple modules are working together.

<br>

- **`settings.py`** is another very important file within the **Project Level**. 
- It is used to make changes at a project scale. Mostly, we will be only changing a files lines for configuration within this file.
-  It stores important data like what is the base dir, what are the secret keys, **debugging True/False**, allowed hosts list, various applications (`in Django, almost function/feature is treated like a application`), middlewares, templates, databases

<br>

- **urls** is another important file within the **Project Level**.
- It is the file which is used for creating routes within the app.
- By default it comes with the admin panel for security. 

- There are many other files which we need to create and add at this Project Level like **`views`** (used to house the functionality of pages and the business logic), **`models`** (used to store the db structure) 