from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include

from config import settings

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="USAT API",
        default_version='v1',
        description="USAT API documentation",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="ilhomjonpersonal@gmail.com"),
        license=openapi.License(name="USAT License"),
    ),
    public=False,
    permission_classes=[permissions.IsAuthenticated],
)

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include('accounts.urls')),
    path('api/docs/swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('api/docs/swagger/', login_required(schema_view.with_ui('swagger', cache_timeout=0)), name='schema-swagger-ui'),
    path('api/docs/redoc/', login_required(schema_view.with_ui('redoc', cache_timeout=0)), name='schema-redoc'),
    path('api/v1/advantages/', include('advantages.urls')),
    path('api/v1/news/', include('news.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
)

if settings.USE_I18N:
    urlpatterns += [
        path('i18n/', include('django.conf.urls.i18n')),
    ]
