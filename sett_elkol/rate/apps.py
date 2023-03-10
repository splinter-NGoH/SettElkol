from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class RateConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sett_elkol.rate'
    verbose_name = _("Rate")
