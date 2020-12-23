from django.core.exceptions import PermissionDenied
from odoo_orm.connection import OdooConnection

odoo = OdooConnection.get_connection()


class OdooUnsafeMixin:

    def dispatch(self, request, *args, **kwargs):
        if not odoo.safe:
            if hasattr(self, 'handle_no_permission'):
                return self.handle_no_permission()
            else:
                raise PermissionDenied()

        return super().dispatch(request, *args, **kwargs)


def odoo_unsafe(f):
    def wrapper(*args, **kwargs):
        if not odoo.safe:
            raise PermissionDenied()

        return f(*args, **kwargs)

    return wrapper
