from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages


def login_view(request):
    """Страница входа. После авторизации редиректит по роли."""
    if request.user.is_authenticated:
        return _redirect_by_role(request.user)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return _redirect_by_role(user)
        else:
            messages.error(request, 'Неверный логин или пароль.')
    else:
        form = AuthenticationForm()

    return render(request, 'auth/login.html', {'form': form})


def logout_view(request):
    """Выход из системы."""
    logout(request)
    return redirect('accounts:login')


def _redirect_by_role(user):
    """Редирект на дашборд в зависимости от роли."""
    if user.is_superadmin:
        return redirect('superadmin:dashboard')
    elif user.is_manager:
        return redirect('crm:dashboard')
    return redirect('accounts:login')
