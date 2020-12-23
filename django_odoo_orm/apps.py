from django.apps import AppConfig
from odoo_orm.connection import OdooConnection

from django_odoo_orm.settings import ODOO_CONNECTION


class DjangoOdooOrm(AppConfig):
    name = 'django_odoo_orm'

    def ready(self):
        odoo = OdooConnection.get_connection()
        odoo.connect(**{k.lower(): v for k, v in ODOO_CONNECTION.items()})
