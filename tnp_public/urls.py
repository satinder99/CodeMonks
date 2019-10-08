"""tnp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from login.views import home_page,search
from django.urls import include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/$', home_page),
    url(r'^$', LoginView.as_view(template_name='login/login.html')),
    url(r'^logout/$', LogoutView.as_view(next_page='/')),
    url(r'^search/', search),
    url(r'^password-reset/', auth_views.PasswordResetView.as_view(template_name='login/password_reset.html'),name = 'password_reset'),
    url(r'^password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='login/password_reset_done.html'),name = 'password_reset_done'),
    url(r'^password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='login/password_reset_confirm.html'),name = 'password_reset_confirm'),
    url(r'^password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='login/password_reset_complete.html'),name = 'password_reset_complete'),
    # For progressive web app

    url('', include('pwa.urls')),
]
