from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class TeachingAssistanceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'qr_code.teaching_assistance'
    verbose_name = _("Teaching Assistance")
