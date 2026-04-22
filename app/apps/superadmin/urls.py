from django.urls import path
from . import views

app_name = 'superadmin'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('companies/', views.companies_list, name='companies'),
    path('companies/<int:pk>/', views.company_detail, name='company_detail'),
    path('companies/create/', views.company_create, name='company_create'),
    path('companies/<int:pk>/edit/', views.company_edit, name='company_edit'),
    path('settings/', views.settings_view, name='settings'),
]
