from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DeliverymanConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sett_elkol.deliveryman'
    verbose_name = _("Delivery Man")
