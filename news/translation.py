from modeltranslation.translator import register, TranslationOptions

from .models import Statistic, Gallery, News


@register(Statistic)
class StatisticTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


@register(Gallery)
class GalleryTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'summary', 'content')
