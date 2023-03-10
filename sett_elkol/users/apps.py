from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "sett_elkol.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import sett_elkol.users.signals  
        except ImportError:
            pass

