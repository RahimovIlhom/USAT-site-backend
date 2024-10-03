from modeltranslation.translator import register, TranslationOptions
from .models import Advantage


@register(Advantage)
class AdvantageTranslationOptions(TranslationOptions):
    fields = ('title', 'content')
