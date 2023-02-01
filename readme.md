# React-Django Prototype Application

## Overview

This is a Django project combining the major features of both frameworks/libraries

## Seed Database

```
python manage.py shell
```

```python
from django_react_app.models import Product

Product.objects.create(name="Football")
Product.objects.create(name="Book")
Product.objects.create(name="Keyboard")
Product.objects.create(name="Bike")
```
