from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path("auth/login.html", views.login_view, name="login"),
    path("crm/dashboard.html", views.crm_dashboard, name="crm_dashboard"),
    path("superadmin/dashboard.html", views.superadmin_dashboard, name="superadmin_dashboard"),
    path("auth/<path:page>", views.section_page, {"section": "auth"}, name="auth_page"),
    path("crm/<path:page>", views.section_page, {"section": "crm"}, name="crm_page"),
    path("superadmin/<path:page>", views.section_page, {"section": "superadmin"}, name="superadmin_page"),
]