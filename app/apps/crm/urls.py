from django.urls import path
from . import views

app_name = 'crm'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('clients/', views.clients_list, name='clients'),
    path('clients/<int:pk>/', views.client_detail, name='client_detail'),
    path('orders/', views.orders_list, name='orders'),
    path('orders/create/', views.order_create, name='order_create'),
    path('orders/<int:pk>/', views.order_detail, name='order_detail'),
    path('finance/', views.finance, name='finance'),
    path('notifications/', views.notifications, name='notifications'),
    path('settings/', views.settings_view, name='settings'),
]
