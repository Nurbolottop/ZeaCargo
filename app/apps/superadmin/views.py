from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from apps.accounts.decorators import superadmin_required
from apps.cargo.models import CargoCompany
from apps.accounts.models import CustomUser
from apps.clients.models import Client
from apps.orders.models import Order


@superadmin_required
def dashboard(request):
    """Дашборд суперадмина — общая статистика платформы."""
    stats = {
        'total_companies': CargoCompany.objects.count(),
        'active_companies': CargoCompany.objects.filter(is_active=True).count(),
        'total_managers': CustomUser.objects.filter(role=CustomUser.Role.MANAGER).count(),
        'total_clients': Client.objects.count(),
        'total_orders': Order.objects.count(),
        'active_orders': Order.objects.exclude(delivery_status='issued').count(),
    }
    companies = CargoCompany.objects.all().order_by('-created_at')[:5]
    return render(request, 'superadmin/dashboard.html', {
        'stats': stats,
        'companies': companies,
    })


@superadmin_required
def companies_list(request):
    """Список всех карго-компаний."""
    companies = CargoCompany.objects.all().order_by('-created_at')
    return render(request, 'superadmin/companies.html', {'companies': companies})


@superadmin_required
def company_detail(request, pk):
    """Детальная страница карго-компании."""
    company = get_object_or_404(CargoCompany, pk=pk)
    managers = CustomUser.objects.filter(cargo_company=company, role=CustomUser.Role.MANAGER)
    clients_count = Client.objects.filter(cargo_company=company).count()
    orders_count = Order.objects.filter(cargo_company=company).count()
    active_orders = Order.objects.filter(
        cargo_company=company
    ).exclude(delivery_status='issued').count()

    return render(request, 'superadmin/company-detail.html', {
        'company': company,
        'managers': managers,
        'clients_count': clients_count,
        'orders_count': orders_count,
        'active_orders': active_orders,
    })


@superadmin_required
def company_create(request):
    """Создание новой карго-компании."""
    from .forms import CargoCompanyForm
    if request.method == 'POST':
        form = CargoCompanyForm(request.POST, request.FILES)
        if form.is_valid():
            company = form.save()
            messages.success(request, f'Карго-компания «{company.name}» успешно создана.')
            return redirect('superadmin:company_detail', pk=company.pk)
    else:
        form = CargoCompanyForm()
    return render(request, 'superadmin/company-form.html', {'form': form, 'action': 'create'})


@superadmin_required
def company_edit(request, pk):
    """Редактирование карго-компании."""
    from .forms import CargoCompanyForm
    company = get_object_or_404(CargoCompany, pk=pk)
    if request.method == 'POST':
        form = CargoCompanyForm(request.POST, request.FILES, instance=company)
        if form.is_valid():
            form.save()
            messages.success(request, 'Данные компании обновлены.')
            return redirect('superadmin:company_detail', pk=company.pk)
    else:
        form = CargoCompanyForm(instance=company)
    return render(request, 'superadmin/company-form.html', {'form': form, 'company': company, 'action': 'edit'})


@superadmin_required
def settings_view(request):
    """Настройки платформы."""
    return render(request, 'superadmin/settings.html', {})
