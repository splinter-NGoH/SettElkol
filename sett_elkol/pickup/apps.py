from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PickupConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sett_elkol.pickup'
    verbose_name = _("Pick Up")
