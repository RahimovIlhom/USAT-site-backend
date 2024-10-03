from django.db import models
from django.utils.translation import gettext_lazy as _


class ActiveObjectManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class EduDirection(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name=_('Author'))
    name = models.CharField(max_length=255, verbose_name=_('Direction name'))
    content = models.TextField(blank=True, null=True, verbose_name=_('Content'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))

    objects = models.Manager()
    active_objects = ActiveObjectManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Edu direction')
        verbose_name_plural = _('Edu directions')


class EduProgram(models.Model):
    edu_type = models.ForeignKey('EduType', on_delete=models.CASCADE, related_name='edu_programs',
                                 verbose_name=_('Edu type'))
    direction = models.ForeignKey(EduDirection, on_delete=models.CASCADE, verbose_name=_('Direction'),
                                  related_name='edu_programs')
    price = models.IntegerField(verbose_name=_('Contract price'))
    study_duration = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True,
                                         verbose_name=_('Study duration'))

    objects = models.Manager()

    def __str__(self):
        return f"{self.edu_type} - {self.price}"

    class Meta:
        verbose_name = _('Edu program')
        verbose_name_plural = _('Edu programs')


class EduType(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name=_('Author'))
    name = models.CharField(max_length=255, verbose_name=_('Type name'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))

    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Edu type')
        verbose_name_plural = _('Edu types')
