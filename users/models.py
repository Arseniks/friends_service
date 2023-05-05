from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    friends = models.ManyToManyField(
        'self',
        through='Relationship',
        symmetrical=False,
        related_name='related_to',
    )


class Relationship(models.Model):
    from_person = models.ForeignKey(
        CustomUser,
        related_name='from_people',
        on_delete=models.CASCADE,
    )
    to_person = models.ForeignKey(
        CustomUser,
        related_name='to_people',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'Дружба {self.from_person} с {self.to_person}'

    class Meta:
        verbose_name = 'взаимоотношение'
        verbose_name_plural = 'взаимоотношения'


class Pending(models.Model):
    sender = models.ForeignKey(
        CustomUser,
        related_name='sender',
        help_text='Пользователь, отправивший заявку',
        on_delete=models.CASCADE,
    )
    recipient = models.ForeignKey(
        CustomUser,
        related_name='recipient',
        help_text='Пользователь, получивший заявку',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'Заявка в друзья {self.recipient} от {self.sender}'

    class Meta:
        verbose_name = 'заявка'
        verbose_name_plural = 'заявки'
