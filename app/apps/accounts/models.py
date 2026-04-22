from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        SUPERADMIN = 'superadmin', 'Суперадминистратор'
        MANAGER = 'manager', 'Менеджер карго'

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.MANAGER,
        verbose_name='Роль'
    )
    cargo_company = models.ForeignKey(
        'cargo.CargoCompany',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='managers',
        verbose_name='Карго-компания'
    )
    phone = models.CharField(
        max_length=20,
        blank=True,
        verbose_name='Телефон'
    )
    avatar = models.ImageField(
        upload_to='avatars/',
        null=True,
        blank=True,
        verbose_name='Аватар'
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['-date_joined']

    def __str__(self):
        return f'{self.get_full_name() or self.username} ({self.get_role_display()})'

    @property
    def is_superadmin(self):
        return self.role == self.Role.SUPERADMIN

    @property
    def is_manager(self):
        return self.role == self.Role.MANAGER
