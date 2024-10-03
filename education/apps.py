from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class EducationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'education'

    verbose_name = _('Education')
    verbose_name_plural = _('Education')
