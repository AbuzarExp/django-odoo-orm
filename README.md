Django Odoo ORM
===============

Django Odoo ORM is a Django app to provide a fully setup ORM to Odoo in any Django project. This project adds nothing
but an app that sets the connection up at startup.

[![Last version](https://img.shields.io/pypi/v/django-odoo-orm)](https://pypi.org/project/django-odoo-orm/)
[![Python versions](https://img.shields.io/pypi/pyversions/django-odoo-orm?color=orange)](https://pypi.org/project/django-odoo-orm/)
[![Django versions](https://img.shields.io/pypi/djversions/django-odoo-orm)](https://pypi.org/project/django-odoo-orm/)
[![Licence](https://img.shields.io/pypi/l/django-odoo-orm)](https://pypi.org/project/django-odoo-orm/)

Quick start
-----------

1. Add "django_odoo_orm" to your INSTALLED_APPS setting like this:

```python
INSTALLED_APPS = [
    # ...
    'django_odoo_orm',
]
```

2. Add "django_odoo_orm.context_processors.odoo_connection" to your TEMPLATES setting like this:

```python
TEMPLATES = [
    {
        # ...
        'OPTIONS': {
            'context_processors': [
                # ...
                'django_odoo_orm.context_processors.odoo_connection',
            ],
        },
    },
]
```
