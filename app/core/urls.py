from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Авторизация
    path('auth/', include('apps.accounts.urls', namespace='accounts')),

    # SuperAdmin
    path('superadmin/', include('apps.superadmin.urls', namespace='superadmin')),

    # CRM (Manager)
    path('crm/', include('apps.crm.urls', namespace='crm')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)