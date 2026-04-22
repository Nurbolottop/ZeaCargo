from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index.html', views.home, name='home_html'),
    path("auth/login/", views.login_view, name="login_alias"),
    path("auth/login.html", views.login_view, name="login"),
    path("bot/simulator/", views.bot_simulator_alias, name="bot_simulator_alias"),
    path("client/catalog/", views.client_catalog_alias, name="client_catalog_alias"),
    path("crm/dashboard/", views.crm_dashboard_alias, name="crm_dashboard_alias"),
    path("crm/dashboard.html", views.crm_dashboard, name="crm_dashboard"),
    path("superadmin/dashboard/", views.superadmin_dashboard_alias, name="superadmin_dashboard_alias"),
    path("superadmin/dashboard.html", views.superadmin_dashboard, name="superadmin_dashboard"),
    path("superadmin/settings/", views.superadmin_settings_alias, name="superadmin_settings_alias"),
    path("superadmin/companies/", views.superadmin_companies_alias, name="superadmin_companies_alias"),
    path("auth/<path:page>", views.section_page, {"section": "auth"}, name="auth_page"),
    path("bot/<path:page>", views.section_page, {"section": "bot"}, name="bot_page"),
    path("client/<path:page>", views.section_page, {"section": "client"}, name="client_page"),
    path("crm/<path:page>", views.section_page, {"section": "crm"}, name="crm_page"),
    path("superadmin/<path:page>", views.section_page, {"section": "superadmin"}, name="superadmin_page"),
]
