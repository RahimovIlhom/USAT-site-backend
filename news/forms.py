from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet, ModelForm, CharField
from django.utils.translation import gettext_lazy as _
from django_ckeditor_5.widgets import CKEditor5Widget

from .models import News


class NewsPhotoInlineFormSet(BaseInlineFormSet):
    def clean(self):
        super().clean()
        if not any(form.cleaned_data for form in self.forms if not form.cleaned_data.get('DELETE', False)):
            raise ValidationError(_('Please enter at least one photo!'))


class NewsAdminForm(ModelForm):
    content = CharField(
        widget=CKEditor5Widget(
            config_name='news',
        )
    )  # TextField uchun CKEditor vidjeti

    class Meta:
        model = News
        fields = '__all__'
