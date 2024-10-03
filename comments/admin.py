from django.contrib import admin

from .models import StudentComment


@admin.register(StudentComment)
class StudentCommentAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'comment', 'created_at')
    search_fields = ('fullname', 'comment', 'email', 'phone')
    ordering = ('-created_at',)
    readonly_fields = ('author',)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        obj.save()
