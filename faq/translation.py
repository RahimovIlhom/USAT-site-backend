from modeltranslation.translator import register, TranslationOptions

from .models import FAQ


@register(FAQ)
class FAQTranslationOptions(TranslationOptions):
    fields = ('question', 'answer')
