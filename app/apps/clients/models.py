from django.db import models


class Client(models.Model):
    cargo_company = models.ForeignKey(
        'cargo.CargoCompany',
        on_delete=models.CASCADE,
        related_name='clients',
        verbose_name='Карго-компания'
    )
    telegram_id = models.BigIntegerField(unique=True, verbose_name='Telegram ID')
    telegram_username = models.CharField(max_length=100, blank=True, verbose_name='Username Telegram')
    full_name = models.CharField(max_length=200, verbose_name='ФИО')
    phone = models.CharField(max_length=50, blank=True, verbose_name='Телефон')
    is_active = models.BooleanField(default=True, verbose_name='Активен')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.full_name} (@{self.telegram_username})'

    def get_total_debt(self):
        from apps.finance.models import Debt
        return Debt.objects.filter(client=self).aggregate(
            total=models.Sum('amount')
        )['total'] or 0
