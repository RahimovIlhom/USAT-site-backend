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


RANK_CHOICES = (
    (0, _('Low')),
    (1, _('Medium')),
    (2, _('High')),
    (3, _('Very high')),
    (4, _('Extreme')),
    (5, _('Critical')),
)

class News(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name=_('Author'))
    title = models.CharField(max_length=500, verbose_name=_('Title'))
    summary = models.CharField(max_length=1000, verbose_name=_('Summary'), blank=True, null=True)
    # content = CKEditor5Field(verbose_name=_('Content'), config_name='extends')
    content = models.TextField(verbose_name=_('Content'), blank=True, null=True)
    photo = models.ImageField(upload_to='news/photos', verbose_name=_('Photo'), blank=True, null=True)
    video_url = models.URLField(verbose_name=_('Video URL'), blank=True, null=True)
    rank = models.IntegerField(default=5, verbose_name=_('Rank'), choices=RANK_CHOICES)
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))

    active_objects = ActiveObjectManager()
    objects = models.Manager()

    class Meta:
        verbose_name = _('News')
        verbose_name_plural = _('News')

    def __str__(self):
        return self.title


class ViewRecord(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='view_records',
                             verbose_name=_('News'))
    ip_address = models.GenericIPAddressField(verbose_name=_('IP Address'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))

    objects = models.Manager()

    class Meta:
        unique_together = ('news', 'ip_address')
