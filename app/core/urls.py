from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('apps.base.urls')),
]


if settings.DEBUG:
    urlpatterns += [
        path(
            'assets/<path:path>',
            serve,
            {'document_root': settings.BASE_DIR / 'static' / 'assets'},
        ),
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
