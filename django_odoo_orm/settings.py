from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

ODOO_CONNECTION = getattr(settings, 'ODOO_CONNECTION')
