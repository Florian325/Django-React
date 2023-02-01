# React-Django Prototype Application

## Intoduction

This is a Django project combining the major features of both frameworks/libraries

## Setup

### Clone project

```
git clone ...
```

### Navigate into the Github project

```
cd Django-React
```

### Create a virtual environment

```
python -m .venv
```

### Activate the virtual environment

```
"./.venv/Scripts/activate" # Command Prompt
./.venv/Scripts/Activate.ps1 # PowerShell
```

### Navigate into the django project

```
cd django_react_roject
```

### Seed Database

```
python manage.py shell
```
(only example data)
```python
from django_react_app.models import Product

Product.objects.create(name="Football")
Product.objects.create(name="Book")
Product.objects.create(name="Keyboard")
Product.objects.create(name="Bike")
```

### Start Server

```
python manage.py runserver
```

The website is now available at localhost:8000
