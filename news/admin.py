from django.contrib import admin
from .models import Statistic, Gallery, News


class StatisticAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'value')
    list_filter = ('is_active', 'author')
    search_fields = ('title', 'content')
    ordering = ('-created_at',)
    exclude = ('is_active', 'author')
    readonly_fields = ('author', 'created_at',)

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


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    list_filter = ('is_active', 'author')
    search_fields = ('title',)
    ordering = ('-created_at',)
    exclude = ('is_active', 'author')
    readonly_fields = ('author', 'created_at',)

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


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    list_filter = ('is_active', 'author')
    search_fields = ('title', 'content')
    ordering = ('-created_at',)
    exclude = ('is_active', 'author')
    readonly_fields = ('author', 'created_at',)

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


admin.site.register(Statistic, StatisticAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(News, NewsAdmin)
