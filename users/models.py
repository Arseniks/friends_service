from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    friends = models.ManyToManyField(
        'self',
        verbose_name='твой друг',
        help_text='Добавь нового друга',
    )


class Pending:
    sender = models.OneToOneField(
        CustomUser,
        verbose_name='отправитель заявки',
        help_text='Пользователь, отправивший заявку',
        on_delete=models.CASCADE,
    )
    recipient = models.OneToOneField(
        CustomUser,
        verbose_name='Получатель заявки',
        help_text='Пользователь, получивший заявку',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'Заявка в друзья {self.recipient} от {self.sender}'

    class Meta:
        verbose_name = 'заявка'
        verbose_name_plural = 'заявки'
