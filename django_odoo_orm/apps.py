from django.apps import AppConfig
from django.conf import settings
from odoo_orm.connection import OdooConnection


class DjangoOdooOrm(AppConfig):
    name = 'django_odoo_orm'

    def ready(self):
        odoo = OdooConnection.get_connection()
        odoo_login = settings.ODOO_LOGIN[settings.ODOO_CURRENT_LOGIN]
        odoo.connect(odoo_login['URL'], odoo_login['DB'], odoo_login['USER'], odoo_login['PASSWORD'])
