from django.http import Http404
from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer

from users.models import CustomUser
from users.models import Relationship


class UserListPostSerializer(ModelSerializer):
    from_person = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    def create(self, validated_data):
        relationship_from_user = Relationship.objects.get_or_create(
            from_person=validated_data['to_person'],
            to_person=validated_data['from_person'],
            status='входящая заявка',
        )[0]
        relationship_from_user.status = 'входящая заявка'
        return super().create(validated_data)

    class Meta:
        model = Relationship
        fields = (
            Relationship.from_person.field.name,
            Relationship.to_person.field.name,
        )


class UserListGetSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            CustomUser.id.field.name,
            CustomUser.username.field.name,
        )


class PendingListDeleteSerializer(ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def get_object(self, to_person_pk):
        try:
            return Relationship.objects.get(
                to_person__pk=to_person_pk,
            )
        except Relationship.DoesNotExist:
            raise Http404

    def destroy(self, request, *args, **kwargs):
        recipient_pk = int(request.data['to_person'])
        sender_pk = int(request.data['from_person'])

        if recipient_pk == self.user:
            relationship_from_request_user = self.get_object(
                sender_pk, recipient_pk
            )
            relationship_from_request_user.delete()
            relationship_to_request_user = self.get_object(
                recipient_pk, sender_pk
            )
            relationship_to_request_user.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    class Meta:
        model = Relationship
        fields = (
            Relationship.from_person.field.name,
            Relationship.to_person.field.name,
        )


class PendingListPutSerializer(ModelSerializer):
    def update(self, instance, validated_data):
        recipient = validated_data['to_person']
        sender = validated_data['from_person']
        relationship = Relationship.objects.get(
            from_person=sender,
            to_person=recipient,
        )
        relationship.status = 'дружба'
        relationship.save()

        return Relationship.objects.update(
            from_person=recipient,
            to_person=sender,
            status='дружба',
        )

    class Meta:
        model = Relationship
        fields = (
            Relationship.from_person.field.name,
            Relationship.to_person.field.name,
        )


class PendingListGetSerializer(ModelSerializer):
    class Meta:
        model = Relationship
        fields = (
            Relationship.id.field.name,
            Relationship.from_person.field.name,
            Relationship.to_person.field.name,
            Relationship.status.field.name,
        )


class FriendsListGetSerializer(ModelSerializer):
    class Meta:
        model = Relationship
        fields = (
            Relationship.id.field.name,
            Relationship.from_person.field.name,
            Relationship.to_person.field.name,
            Relationship.status.field.name,
        )


class FriendsListDeleteSerializer(ModelSerializer):
    from_person = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    def get_object(self, from_person_pk, to_person_pk):
        try:
            return Relationship.objects.get(
                from_person__pk=from_person_pk,
                to_person__pk=to_person_pk,
            )
        except Relationship.DoesNotExist:
            raise Http404

    def destroy(self, request, *args, **kwargs):
        recipient_pk = int(request.data['pk'])
        sender_pk = int(request.data['from_person'])

        relationship_from_request_user = self.get_object(
            sender_pk, recipient_pk
        )
        relationship_from_request_user.delete()
        relationship_to_request_user = self.get_object(recipient_pk, sender_pk)
        relationship_to_request_user.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    class Meta:
        model = Relationship
        fields = (
            Relationship.id.field.name,
            Relationship.from_person.field.name,
            Relationship.to_person.field.name,
            Relationship.status.field.name,
        )
