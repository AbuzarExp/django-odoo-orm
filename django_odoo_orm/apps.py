from django.apps import AppConfig
from odoo_orm.connection import OdooConnection

from django_odoo_orm.settings import ODOO_CONNECTION, ODOO_CONNECTION_CONNECT_AT_STARTUP


class DjangoOdooOrm(AppConfig):
    name = 'django_odoo_orm'

    def ready(self):
        if ODOO_CONNECTION_CONNECT_AT_STARTUP:
            OdooConnection.get_connection().connect(**{k.lower(): v for k, v in ODOO_CONNECTION.items()})
