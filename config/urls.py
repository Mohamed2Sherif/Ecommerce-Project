"""
URL configuration for OLA_Store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from src.users.auth import views as auth_views
from dj_rest_auth.views import PasswordResetConfirmView

urlpatterns = [
    path(
        "password-reset/confirm/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path("admin/", admin.site.urls),
    path("products/", include("src.products.urls")),
    path(
        "dj-rest-auth/registration/verify-email/",
        auth_views.verify_otp_mail.as_view(),
        name="account_otp_verification_sent",
    ),
    path(
        "dj-rest-auth/registration/",
        auth_views.CustomRegisterView.as_view(),
        name="rest_register",
    ),
    path("dj-rest-auth/", include("dj_rest_auth.urls")),
    path("dj-rest-auth/registration/", include("dj_rest_auth.registration.urls")),
    path("product/", include("src.products.urls")),
    path("orders/", include("src.orders.urls")),
]
