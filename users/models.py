from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


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
        related_name='from_person',
        on_delete=models.CASCADE,
    )
    to_person = models.ForeignKey(
        CustomUser,
        related_name='to_person',
        on_delete=models.CASCADE,
    )

    class Status(models.TextChoices):
        EMPTY = 'нет', _('Нет')
        OUTGOING_REQUEST = 'исходящая заявка', _('Исходящая заявка')
        INCOMING_REQUEST = 'входящая заявка', _('Входящая заявка')
        FRIENDSHIP = 'дружба', _('Дружба')

    status = models.CharField(
        verbose_name='статус отношений',
        help_text='Какие у вас взаимоотношения с этим пользователем',
        max_length=16,
        choices=Status.choices,
        default=Status.OUTGOING_REQUEST,
    )

    def __str__(self):
        return f'Дружба {self.from_person} с {self.to_person}'

    class Meta:
        verbose_name = 'взаимоотношение'
        verbose_name_plural = 'взаимоотношения'
