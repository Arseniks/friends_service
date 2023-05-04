from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import urls
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include
from django.urls import path
from drf_spectacular.views import SpectacularAPIView
from drf_spectacular.views import SpectacularSwaggerView

import home.urls
import users.urls

urlpatterns = [
    path(
        'admin/',
        admin.site.urls,
    ),
    path(
        '',
        include(home.urls),
    ),
    path(
        'auth/',
        include(users.urls),
    ),
    path(
        'auth/',
        include(urls),
    ),
]


if settings.DEBUG:
    import debug_toolbar

    urlpatterns += (
        path('__debug__/', include(debug_toolbar.urls)),
        path(
            'api/schema/',
            SpectacularAPIView.as_view(),
            name='schema',
        ),
        path(
            'api/schema/swagger-ui/',
            SpectacularSwaggerView.as_view(url_name='schema'),
            name='swagger-ui',
        ),
    )

    if hasattr(settings, 'MEDIA_ROOT'):
        urlpatterns += static(
            settings.MEDIA_URL,
            document_root=settings.MEDIA_ROOT,
        )
    else:
        urlpatterns += staticfiles_urlpatterns()
