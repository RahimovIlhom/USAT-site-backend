from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AcademicConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'academic'

    verbose_name = _('Academic')
    verbose_name_plural = _('Academics')
