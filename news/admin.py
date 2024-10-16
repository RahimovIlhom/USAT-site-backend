from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin

from .forms import NewsPhotoInlineFormSet
from .models import Statistic, Gallery, NewsCategory, News, NewsPhoto


@admin.register(Statistic, site=admin.site)
class StatisticAdmin(TabbedTranslationAdmin):
    list_display = ('title', 'author', 'created_at', 'value')
    list_filter = ('is_active', 'author')
    search_fields = ('title', 'content')
    ordering = ('-created_at',)
    exclude = ('is_active', 'author')
    readonly_fields = ('author',)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        obj.save()

    def delete_model(self, request, obj):
        obj.is_active = False
        obj.save()

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(is_active=True)


@admin.register(Gallery, site=admin.site)
class GalleryAdmin(TabbedTranslationAdmin):
    list_display = ('title', 'author', 'created_at')
    list_filter = ('is_active', 'author')
    search_fields = ('title',)
    ordering = ('-created_at',)
    exclude = ('is_active', 'author')
    readonly_fields = ('author',)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        obj.save()

    def delete_model(self, request, obj):
        obj.is_active = False
        obj.save()

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(is_active=True)


@admin.register(NewsCategory, site=admin.site)
class NewsCategoryAdmin(TabbedTranslationAdmin):
    list_display = ('title', 'author', 'created_at')
    list_filter = ('author', )
    search_fields = ('name',)
    ordering = ('-created_at',)
    exclude = ('is_active', 'author')
    readonly_fields = ('author',)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        obj.save()

    def delete_model(self, request, obj):
        obj.is_active = False
        obj.save()

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(is_active=True)


class NewsPhotoInline(admin.TabularInline):
    model = NewsPhoto
    extra = 4
    max_num = 10
    show_change_link = True
    # formset = NewsPhotoInlineFormSet


@admin.register(News, site=admin.site)
class NewsAdmin(TabbedTranslationAdmin):
    list_display = ('title', 'author', 'created_at')
    list_filter = ('is_active', 'author')
    search_fields = ('title', 'content')
    ordering = ('-created_at',)
    exclude = ('is_active', 'author', 'slug')
    readonly_fields = ('author',)
    inlines = [NewsPhotoInline]

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        obj.save()

    def delete_model(self, request, obj):
        obj.is_active = False
        obj.save()

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(is_active=True)
