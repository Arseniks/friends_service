from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView

from users.models import CustomUser
from users.models import Relationship
from users.serializers import FriendsListDeleteSerializer
from users.serializers import FriendsListGetSerializer
from users.serializers import PendingListDeleteSerializer
from users.serializers import PendingListGetSerializer
from users.serializers import PendingListPutSerializer
from users.serializers import UserListGetSerializer
from users.serializers import UserListPostSerializer


class UserListAPIView(ListCreateAPIView):
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UserListGetSerializer
        else:
            return UserListPostSerializer

    def get_queryset(self):
        ids = Relationship.objects.filter(
            from_person__pk=self.request.user.pk,
            status__in=('дружба', 'исходящая заявка'),
        ).values_list(
            f'{Relationship.to_person.field.name}__{CustomUser.id.field.name}',
        )
        return CustomUser.objects.exclude(pk__in=ids).exclude(
            id=self.request.user.pk
        )


class PendingListAPIView(viewsets.ModelViewSet):
    http_method_names = ['get', 'delete', 'put']

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PendingListGetSerializer
        elif self.request.method == 'PUT':
            return PendingListPutSerializer
        else:
            return PendingListDeleteSerializer

    def get_queryset(self):
        return Relationship.objects.filter(
            from_person__pk=self.request.user.pk,
            status='исходящая заявка',
        ) | Relationship.objects.filter(
            to_person__pk=self.request.user.pk,
            status='исходящая заявка',
        )


class FriendsListAPIView(viewsets.ModelViewSet):
    http_method_names = ['get', 'delete']

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return FriendsListGetSerializer
        else:
            return FriendsListDeleteSerializer

    def get_queryset(self):
        return Relationship.objects.filter(
            to_person__pk=self.request.user.pk,
            status='дружба',
        )
