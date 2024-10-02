from django import forms
from django.core.exceptions import ValidationError
from .models import EduType


class EduTypeInlineFormSet(forms.BaseInlineFormSet):
    def clean(self):
        super().clean()
        # Check if at least one EduType is provided
        if not any(form.cleaned_data for form in self.forms if not form.cleaned_data.get('DELETE', False)):
            raise ValidationError('Kamida bitta EduType ni to\'ldirishingiz kerak.')
