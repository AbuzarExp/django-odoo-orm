from odoo_orm.connection import OdooConnection


def odoo_connection(request):
    return {
        'ODOO_CONNECTION': OdooConnection.get_connection(),
    }
