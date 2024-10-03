from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class FaqConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'faq'

    verbose_name = _('FAQ')
    verbose_name_plural = _('FAQs')
