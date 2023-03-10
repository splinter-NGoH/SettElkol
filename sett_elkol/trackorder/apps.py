from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TrackorderConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sett_elkol.trackorder'
    verbose_name = _("Track Order")
