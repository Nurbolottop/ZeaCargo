from django.shortcuts import render, get_object_or_404, redirect
from apps.accounts.decorators import manager_required
from apps.clients.models import Client
from apps.orders.models import Order
from apps.finance.models import Payment


@manager_required
def dashboard(request):
    """Дашборд менеджера карго-компании."""
    company = request.user.cargo_company
    stats = {
        'total_clients': Client.objects.filter(cargo_company=company).count(),
        'total_orders': Order.objects.filter(cargo_company=company).count(),
        'in_transit': Order.objects.filter(cargo_company=company, delivery_status='in_transit').count(),
        'ready': Order.objects.filter(cargo_company=company, delivery_status='ready').count(),
        'unpaid': Order.objects.filter(cargo_company=company, payment_status='unpaid').count(),
    }
    recent_orders = Order.objects.filter(cargo_company=company).order_by('-created_at')[:10]
    recent_payments = Payment.objects.filter(cargo_company=company).order_by('-created_at')[:5]

    return render(request, 'crm/dashboard.html', {
        'stats': stats,
        'recent_orders': recent_orders,
        'recent_payments': recent_payments,
        'company': company,
    })


@manager_required
def clients_list(request):
    company = request.user.cargo_company
    q = request.GET.get('q', '')
    clients = Client.objects.filter(cargo_company=company)
    if q:
        clients = clients.filter(full_name__icontains=q) | clients.filter(phone__icontains=q)
    return render(request, 'crm/clients/index.html', {'clients': clients, 'q': q})


@manager_required
def client_detail(request, pk):
    company = request.user.cargo_company
    client = get_object_or_404(Client, pk=pk, cargo_company=company)
    orders = Order.objects.filter(client=client)
    payments = Payment.objects.filter(client=client)
    return render(request, 'crm/clients/detail.html', {
        'client': client,
        'orders': orders,
        'payments': payments,
    })


@manager_required
def orders_list(request):
    company = request.user.cargo_company
    orders = Order.objects.filter(cargo_company=company).select_related('client')
    status = request.GET.get('status', '')
    if status:
        orders = orders.filter(delivery_status=status)
    return render(request, 'crm/orders/index.html', {
        'orders': orders,
        'status_filter': status,
        'delivery_statuses': Order.DeliveryStatus.choices,
    })


@manager_required
def order_create(request):
    company = request.user.cargo_company
    if request.method == 'POST':
        from .forms import OrderForm
        form = OrderForm(request.POST, cargo_company=company)
        if form.is_valid():
            order = form.save(commit=False)
            order.cargo_company = company
            order.save()
            return redirect('crm:order_detail', pk=order.pk)
    else:
        from .forms import OrderForm
        form = OrderForm(cargo_company=company)
    return render(request, 'crm/orders/create.html', {'form': form})


@manager_required
def order_detail(request, pk):
    company = request.user.cargo_company
    order = get_object_or_404(Order, pk=pk, cargo_company=company)
    return render(request, 'crm/orders/detail.html', {'order': order})


@manager_required
def finance(request):
    company = request.user.cargo_company
    payments = Payment.objects.filter(cargo_company=company).select_related('client', 'order')
    return render(request, 'crm/finance/index.html', {'payments': payments})


@manager_required
def notifications(request):
    return render(request, 'crm/notifications/index.html', {})


@manager_required
def settings_view(request):
    return render(request, 'crm/settings/index.html', {'company': request.user.cargo_company})
