from django.db import models
from django.utils.translation import gettext_lazy as _

from education.models import ActiveObjectManager


class Advantage(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name=_('Author'))
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    content = models.TextField(verbose_name=_('Content'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))

    active_objects = ActiveObjectManager()
    objects = models.Manager()

    class Meta:
        verbose_name = _('Advantage')
        verbose_name_plural = _('Advantages')

    def __str__(self):
        return self.title
