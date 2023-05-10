from django.conf import settings
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.urls import re_path
import djoser.urls
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

import users.urls

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path(
        'admin/',
        admin.site.urls,
    ),
    path(
        '',
        include(users.urls),
    ),
    path('auth/', include(djoser.urls)),
    re_path(
        r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json',
    ),
    re_path(
        r'^swagger/$',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui',
    ),
    re_path(
        r'^redoc/$',
        schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc',
    ),
]


if settings.DEBUG:
    import debug_toolbar

    urlpatterns += (
        path(
            '__debug__/',
            include(debug_toolbar.urls),
        ),
    )
