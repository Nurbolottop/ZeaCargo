from functools import wraps
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib import messages


def superadmin_required(view_func):
    """Разрешает доступ только суперадминистраторам платформы."""
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        if not request.user.is_superadmin:
            messages.error(request, 'Доступ запрещён.')
            return redirect('accounts:login')
        return view_func(request, *args, **kwargs)
    return wrapper


def manager_required(view_func):
    """Разрешает доступ менеджерам карго-компаний."""
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        if not request.user.is_manager:
            # Суперадмин пытается зайти в CRM — отправляем в его кабинет
            if request.user.is_superadmin:
                return redirect('superadmin:dashboard')
            logout(request)
            messages.error(request, 'Доступ запрещён.')
            return redirect('accounts:login')
        if not request.user.cargo_company:
            # Менеджер без компании — показываем ошибку, не зацикливаем
            from django.http import HttpResponse
            return HttpResponse(
                '<h2 style="font-family:sans-serif;padding:40px;color:#EF4444;">'
                '⚠️ Ваш аккаунт не привязан к карго-компании. '
                'Обратитесь к суперадминистратору.</h2>'
                '<a href="/auth/logout/" style="font-family:sans-serif;padding:40px;display:block;">Выйти</a>',
                status=403
            )
        return view_func(request, *args, **kwargs)
    return wrapper



def login_required_any(view_func):
    """Разрешает доступ любому авторизованному пользователю системы."""
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        return view_func(request, *args, **kwargs)
    return wrapper
