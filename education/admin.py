from django.contrib import admin

from .forms import EduTypeInlineFormSet
from .models import EduDirection, EduType, EduProgram


class EduTypeInline(admin.TabularInline):
    model = EduProgram
    extra = 1
    formset = EduTypeInlineFormSet


@admin.register(EduDirection)
class EduDirectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'created_at')
    list_filter = ('is_active', )
    search_fields = ('name', 'description')
    exclude = ('is_active', 'author')
    readonly_fields = ('author',)
    inlines = [EduTypeInline]

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        obj.save()


@admin.register(EduType)
class EduTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'created_at')
    search_fields = ('name', )
    exclude = ('author', )
    readonly_fields = ('author',)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        obj.save()
