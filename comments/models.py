from django.db import models
from django.utils.translation import gettext_lazy as _


class StudentComment(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name=_('Author'))
    photo = models.ImageField(upload_to='comment/students', verbose_name=_('Photo'), null=True, blank=True)
    fullname = models.CharField(max_length=255, verbose_name=_('Fullname'))
    email = models.EmailField(verbose_name=_('Email'), blank=True, null=True)
    phone = models.CharField(max_length=20, verbose_name=_('Phone'), blank=True, null=True)
    comment = models.TextField(verbose_name=_('Comment'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))

    objects = models.Manager()

    class Meta:
        verbose_name = _('Student comment')
        verbose_name_plural = _('Student comments')

    def __str__(self):
        return self.fullname
