from django.contrib.auth import logout
from django.shortcuts import redirect
from django.utils.translation import get_language


def basic_logout(request):
    logout(request)
    next_page = request.GET.get('next', '/api-auth/login/')
    return redirect(next_page)


def redirect_admin(request):
    current_language = get_language()
    print(current_language)
    if not current_language:
        current_language = 'uz'
    return redirect(f'/{current_language}/admin')
