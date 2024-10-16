from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from django.utils.translation import gettext_lazy as _


class NewsPhotoInlineFormSet(BaseInlineFormSet):
    def clean(self):
        super().clean()
        if not any(form.cleaned_data for form in self.forms if not form.cleaned_data.get('DELETE', False)):
            raise ValidationError(_('Please enter at least one photo!'))
