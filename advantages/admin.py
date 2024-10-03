from django.contrib import admin
from .models import Advantage


class AdvantageAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
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


admin.site.register(Advantage, AdvantageAdmin)
