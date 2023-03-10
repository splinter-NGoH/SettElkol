from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ChefConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sett_elkol.chef'
    verbose_name = _("Chef")