import os

from corsheaders.defaults import default_headers
from django.utils.translation import gettext_lazy as _
from pathlib import Path
from environs import Env

env = Env()
env.read_env()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = env.str('SECRET_KEY')

DEBUG = env.bool('DEBUG', default=False)

ALLOWED_HOSTS = ['*']
# ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['*'])

# SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

CSRF_TRUSTED_ORIGINS = env.list('CSRF_TRUSTED_ORIGINS', default=['*'])


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',

    # global apps
    'ckeditor',
    'ckeditor_uploader',
    'drf_yasg',
    'rest_framework',
    'corsheaders',
    'django_ckeditor_5',

    # local apps
    'accounts.apps.AccountsConfig',
    'education.apps.EducationConfig',
    'academic.apps.AcademicConfig',
    'news.apps.NewsConfig',
    'advantages.apps.AdvantagesConfig',
    'comments.apps.CommentsConfig',
    'faq.apps.FaqConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'accounts.middleware.CheckSecretMiddleware',
]

ROOT_URLCONF = 'config.urls'

# REST FRAMEWORK
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    'DEFAULT_RENDERER_CLASSES': (
            'rest_framework.renderers.JSONRenderer',
        ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'accounts.permissions.HasXSecretPermission',
        # 'rest_framework.permissions.AllowAny',
        # 'rest_framework.permissions.IsAuthenticated',
    ),
}

SWAGGER_SETTINGS = {
    'USE_SESSION_AUTH': True,
    'USE_JSON_EDITOR': True,
    'LOGIN_URL': '/api-auth/login/',
    'LOGOUT_URL': '/accounts/logout/',
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header',
        }
    },
    'DEFAULT_GENERATOR_CLASS': 'drf_yasg.generators.OpenAPISchemaGenerator',
    'SUPPORTED_SUBMIT_METHODS': ['get', 'post', 'put', 'delete', 'patch'],
    'DEFAULT_API_URL': env.str('DEFAULT_API_URL'),
    'DOC_EXPANSION': 'none',
    'OPERATIONS_SORTER': None,
}


LOGIN_URL = '/api-auth/login/'
LOGIN_REDIRECT_URL = '/api/docs/swagger/'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_HEADERS = list(default_headers) + [
    'Accept-Language',
    'X-Secret',
]

# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Database MySQL
# DATABASES = {
#     'default': {
#         'ENGINE': "django.db.backends.mysql",
#         'NAME': env.str('DB_NAME'),
#         'USER': env.str('DB_USER'),
#         'PASSWORD': env.str('DB_PASSWORD'),
#         'HOST': env.str('DB_HOST'),
#         'PORT': env.str('DB_PORT')
#     }
# }


# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

JAZZMIN_SETTINGS = {
    "site_title": "USAT Admin",
    "site_header": "USAT site",
    "site_brand": "USAT Admin",
    "site_logo": "imgs/logo.jpg",
    "login_logo": "imgs/logo.webp",
    "login_logo_dark": "imgs/logo.jpg",
    "site_logo_classes": "img-circle",
    "site_icon": "imgs/icon.png",
    "welcome_sign": "Welcome to the USAT admin site",
    "copyright": "Copyright by the USAT",
    "user_avatar": None,

    ############
    # Top Menu #
    ############
    "topmenu_links": [
        {"name": _("Home"), "url": "admin:index", "permissions": ["auth.view_user"]},
    ],

    #############
    # Side Menu #
    #############
    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": [],
    "hide_models": [],

    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "news.NewsCategory": "fas fa-folder",
        "news.News": "fas fa-newspaper",
        "news.Gallery": "fas fa-images",
        "news.Statistic": "fas fa-chart-pie",
        "advantages.Advantage": "fas fa-star",
        "comments.StudentComment": "fas fa-comments",
        "faq.Faq": "fas fa-question",
        "academic.Academic": "fas fa-university",
        "education.EduDirection": "fas fa-graduation-cap",
        "education.EduProgram": "fas fa-book",
        "education.EduType": "fas fa-layer-group",
    },
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

    #################
    # Related Modal #
    #################
    "related_modal_active": False,

    #############
    # UI Tweaks #
    #############
    "custom_css": None,
    "custom_js": None,
    "use_google_fonts_cdn": True,
    "show_ui_builder": False,

    ###############
    # Change view #
    ###############
    "changeform_format": "carousel",
    "language_chooser": True,
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": False,
    "accent": "accent-lightblue",
    "navbar": "navbar-white navbar-light",
    "no_navbar_border": False,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": True,
    "sidebar": "sidebar-dark-warning",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "lumen",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-outline-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-outline-info",
        "warning": "btn-outline-warning",
        "danger": "btn-outline-danger",
        "success": "btn-outline-success"
    },
    "actions_sticky_top": True
}

# Internationalization

LANGUAGE_CODE = 'uz-UZ'

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_TZ = True
USE_L10N = True

LANGUAGES = [
    ('uz', _('Uzbek')),
    ('en', _('English')),
    ('ru', _('Russian')),
]

LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

MODELTRANSLATION_DEFAULT_LANGUAGE = 'uz'
MODELTRANSLATION_LANGUAGES = ('uz', 'en', 'ru')


# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# CKEditor configurations

CKEDITOR_BASEPATH = STATIC_URL + 'ckeditor/ckeditor/'

CKEDITOR_UPLOAD_PATH = "uploads/"

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
    },
}

CKEDITOR_FILENAME_GENERATOR = 'utils.get_filename'
CKEDITOR_UPLOAD_SLUGIFY_FILENAME = False
CKEDITOR_RESTRICT_BY_USER = True
CKEDITOR_BROWSE_SHOW_DIRS = True
CKEDITOR_RESTRICT_BY_DATE = True
CKEDITOR_STORAGE_BACKEND = 'django.core.files.storage.FileSystemStorage'
CKEDITOR_IMAGE_BACKEND = 'pillow'
PillowBackend = 'pillow.backends.ResizeImageBackend'
CKEDITOR_THUMBNAIL_SIZE = (300, 300)
CKEDITOR_IMAGE_QUALITY = 40
CKEDITOR_FORCE_JPEG_COMPRESSION = True
SILENCED_SYSTEM_CHECKS = ['ckeditor.W001']

# CKEditor5 configurations

CKEDITOR_5_ALLOW_ALL_FILE_TYPES = True
CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 'auto',
        'width': '100%',
        'extraPlugins': ','.join([
            'image2',
            'autolink',
            'code',
            'table',
            'emoji',
        ]),
    },
    'faq': {
        'config': 'default',
    },
    'extends': {
        'config': 'default',
    },
    'news': {
        'config': 'default',
    },
}

CKEDITOR_5_FILE_UPLOAD_PERMISSION = "staff"

# Default primary key field type

AUTH_USER_MODEL = 'auth.User'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Django caches clear
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
        'TIMEOUT': 7200,  # Kesh 2 soat davomida saqlanadi, keyin tozalanadi
    }
}
