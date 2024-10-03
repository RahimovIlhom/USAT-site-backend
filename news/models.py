from django.db import models
from django.utils.translation import gettext_lazy as _
from django_ckeditor_5.fields import CKEditor5Field

from education.models import ActiveObjectManager


class Statistic(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name=_('Author'))
    photo = models.ImageField(upload_to='news/statistics', verbose_name=_('Photo'))
    title = models.CharField(max_length=500, verbose_name=_('Title'))
    value = models.CharField(max_length=20, verbose_name=_('Value'))
    content = models.TextField(verbose_name=_('Content'), blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))

    active_objects = ActiveObjectManager()
    objects = models.Manager()

    class Meta:
        verbose_name = _('Statistic')
        verbose_name_plural = _('Statistics')

    def __str__(self):
        return self.title


class Gallery(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name=_('Author'))
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    photo = models.ImageField(upload_to='news/galleries', verbose_name=_('Photo'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))

    active_objects = ActiveObjectManager()
    objects = models.Manager()

    class Meta:
        verbose_name = _('Gallery')
        verbose_name_plural = _('Galleries')

    def __str__(self):
        return self.title


class News(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name=_('Author'))
    title = models.CharField(max_length=500, verbose_name=_('Title'))
    content = CKEditor5Field(verbose_name=_('Content'), config_name='extends')
    photo = models.ImageField(upload_to='news/photos', verbose_name=_('Photo'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))

    active_objects = ActiveObjectManager()
    objects = models.Manager()

    class Meta:
        verbose_name = _('News')
        verbose_name_plural = _('News')

    def __str__(self):
        return self.title
