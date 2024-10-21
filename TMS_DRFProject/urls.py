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
from django.contrib import admin
from django.urls import path, include
from djoser.views import TokenCreateView, TokenDestroyView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/", include("notes.api.urls")),
    path("api/v1/users/", include("users.api.urls")),
    path("api/auth/token/", TokenCreateView.as_view(), name="token_create"),
    path("api/auth/token/destroy/", TokenDestroyView.as_view(), name="token_destroy"),
]
