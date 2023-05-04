from django.contrib.auth.decorators import login_required
import django.contrib.auth.views
from django.urls import path

import users.views

app_name = 'users'

urlpatterns = [
    path(
        'login/',
        django.contrib.auth.views.LoginView.as_view(
            template_name='users/login.html',
            redirect_authenticated_user=True,
        ),
        name='login',
    ),
    path(
        'logout/',
        django.contrib.auth.views.LogoutView.as_view(
            template_name='users/logout.html',
        ),
        name='logout',
    ),
    path(
        'signup/',
        users.views.Register.as_view(
            template_name='users/signup.html',
        ),
        name='signup',
    ),
]
