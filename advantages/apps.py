from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AdvantagesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'advantages'

    verbose_name = _('Advantages')
    verbose_name_plural = _('Advantages')
