from django.db import models
from django.utils.translation import gettext_lazy as _


class ActiveObjectManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class EduDirection(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name=_('Author'))
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    description = models.TextField(blank=True, null=True, verbose_name=_('Description'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))

    objects = models.Manager()
    active_objects = ActiveObjectManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Edu direction')
        verbose_name_plural = _('Edu directions')


class EduType(models.Model):
    edu_type_name = models.ForeignKey('EduTypeName', on_delete=models.CASCADE, related_name='edu_types', verbose_name=_('Edu type name'))
    direction = models.ForeignKey(EduDirection, on_delete=models.CASCADE, verbose_name=_('Direction'))
    price = models.IntegerField(verbose_name=_('Price'))
    study_duration = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True, verbose_name=_('Study duration'))

    objects = models.Manager()

    def __str__(self):
        return f"{self.edu_type_name} - {self.price}"

    class Meta:
        verbose_name = _('Edu type')
        verbose_name_plural = _('Edu types')


class EduTypeName(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name=_('Author'))
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))

    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Edu type name')
        verbose_name_plural = _('Edu type names')
