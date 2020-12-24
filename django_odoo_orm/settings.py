from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

ODOO_CONNECTION = getattr(settings, 'ODOO_CONNECTION')

ODOO_CONNECTION_CONNECT_AT_STARTUP = getattr(settings, 'ODOO_CONNECTION_CONNECT_AT_STARTUP', True)
