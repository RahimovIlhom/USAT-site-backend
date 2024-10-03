from django.contrib import admin

from .models import FAQ


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'author', 'created_at')
    list_filter = ('author', 'is_active', )
    search_fields = ('question', 'answer')
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
