from django.contrib import admin

from .forms import EduTypeInlineFormSet
from .models import EduDirection, EduType, EduTypeName


class EduTypeInline(admin.TabularInline):
    model = EduType
    extra = 1
    formset = EduTypeInlineFormSet


@admin.register(EduDirection)
class EduDirectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'created_at')
    list_filter = ('is_active', )
    search_fields = ('name', 'description')
    exclude = ('is_active', 'author')
    inlines = [EduTypeInline]

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        obj.save()


@admin.register(EduTypeName)
class EduTypeNameAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'created_at')
    search_fields = ('name', )
    exclude = ('author', )

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        obj.save()
