from django.db import models
from django.db.models import TextField
from django.urls import reverse
from django.utils.text import slugify
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


class NewsCategory(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name=_('Author'))
    title = models.CharField(max_length=255, verbose_name=_('Category title'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))

    active_objects = ActiveObjectManager()
    objects = models.Manager()

    class Meta:
        verbose_name = _('News category')
        verbose_name_plural = _('News categories')

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
    category = models.ForeignKey(NewsCategory, on_delete=models.SET_NULL, verbose_name=_('Category'), null=True, blank=False)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name=_('Author'))
    title = models.CharField(max_length=500, verbose_name=_('Title'))
    summary = models.CharField(max_length=1000, verbose_name=_('Summary'), blank=True, null=True)
    slug = models.SlugField(max_length=500, verbose_name=_('Slug'), unique=True, blank=True, null=True)
    content = models.TextField(verbose_name=_('Content'), blank=True, null=True)
    content2 = TextField(verbose_name=_('Second content'), blank=True, null=True)
    photo = models.ImageField(upload_to='news/photos', verbose_name=_('Photo'), blank=False, null=True)
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

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('get_news_detail', kwargs={'slug': self.slug})


class ViewRecord(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='view_records',
                             verbose_name=_('News'))
    ip_address = models.GenericIPAddressField(verbose_name=_('IP Address'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))

    objects = models.Manager()

    class Meta:
        unique_together = ('news', 'ip_address')


class NewsPhoto(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, verbose_name=_('News'), related_name='photos')
    photo = models.ImageField(upload_to='news/images', verbose_name=_('Photo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))

    objects = models.Manager()

    class Meta:
        verbose_name = _('News image')
        verbose_name_plural = _('News images')


# class NewsLike(models.Model):
#     news = models.ForeignKey(News, on_delete=models.CASCADE, verbose_name=_('News'))
#     user = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name=_('User'))
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))
#
#     objects = models.Manager()
#
#     class Meta:
#         unique_together = ('news', 'user')
#         verbose_name = _('News like')
#         verbose_name_plural = _('News likes')
#
#
# class NewsComment(models.Model):
#     news = models.ForeignKey(News, on_delete=models.CASCADE, verbose_name=_('News'))
#     user = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name=_('User'))
#     content = models.TextField(verbose_name=_('Content'))
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))
#
#     objects = models.Manager()
#
#     class Meta:
#         verbose_name = _('News comment')
#         verbose_name_plural = _('News comments')
