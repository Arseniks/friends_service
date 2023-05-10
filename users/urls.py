import django.contrib.auth.views
from django.urls import path

import users.views

app_name = 'users'

urlpatterns = [
    django.urls.path(
        'api/v1/user_list/',
        users.views.UserListAPIView.as_view(),
        name='user_list',
    ),
    django.urls.path(
        'api/v1/pending_list/',
        users.views.PendingListAPIView.as_view({'get': 'list'}),
        name='pending_list',
    ),
    django.urls.path(
        'api/v1/pending_list/delete/<int:pk>/',
        users.views.PendingListAPIView.as_view({'delete': 'destroy'}),
        name='pending_list_delete',
    ),
    django.urls.path(
        'api/v1/pending_list/accept/<int:pk>/',
        users.views.PendingListAPIView.as_view({'put': 'update'}),
        name='pending_list_accept',
    ),
    django.urls.path(
        'api/v1/friend_list/',
        users.views.FriendsListAPIView.as_view({'get': 'list'}),
        name='friend_list',
    ),
    django.urls.path(
        'api/v1/friend_list/delete/<int:pk>/',
        users.views.FriendsListAPIView.as_view({'delete': 'destroy'}),
        name='friend_list_delete',
    ),
]
