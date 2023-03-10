from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ShipmentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sett_elkol.shipment'
    verbose_name = _("shipment")
