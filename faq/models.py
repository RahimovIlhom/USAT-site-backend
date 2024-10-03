from django.db import models
from django.utils.translation import gettext_lazy as _
from django_ckeditor_5.fields import CKEditor5Field

from education.models import ActiveObjectManager


class FAQ(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name=_('Author'))
    question = models.CharField(max_length=255, verbose_name=_('Question'))
    # answer = CKEditor5Field(verbose_name=_('Answer'), config_name='faq')
    answer = models.TextField(verbose_name=_('Answer'), blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))

    active_objects = ActiveObjectManager()
    objects = models.Manager()

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = _('FAQ')
        verbose_name_plural = _('FAQs')
        ordering = ['-created_at']
