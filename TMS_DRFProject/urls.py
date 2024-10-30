"""
URL configuration for TMS_DRFProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from debug_toolbar.toolbar import debug_toolbar_urls
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from djoser.views import TokenCreateView, TokenDestroyView
from django.conf import settings
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("notes.api.urls")),
    path("api/v1/users/", include("users.api.urls")),
    # Token
    path("api/auth/token/", TokenCreateView.as_view(), name="token_create"),
    path("api/auth/token/destroy/", TokenDestroyView.as_view(), name="token_destroy"),
    # JWT
    path("api/jwt/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/jwt/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/jwt/verify/", TokenVerifyView.as_view(), name="token_verify"),
    # JSON SCHEMA
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    # Optional UI:
    path(
        "api/docs", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"
    ),
    path("api/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]


if settings.DEBUG:
    # Debug only
    urlpatterns += debug_toolbar_urls()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
