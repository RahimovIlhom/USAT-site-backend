from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import BasePermission
from django.utils.translation import activate
from environs import Env


env = Env()
env.read_env()


class HasXSecretPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

        secret = request.headers.get('X-Secret')

        lang = request.headers.get('Accept-Language', 'uz')
        activate(lang)

        RESPONSES = {
            'uz': 'X-Secret headeri noto\'g\'ri kiritildi.',
            'en': 'The X-Secret header is incorrect.',
            'ru': 'Заголовок X-Secret введен неверно.',
        }

        if secret != env.str('YOUR_SECRET_VALUE'):
            raise PermissionDenied(RESPONSES[lang])

        return True
