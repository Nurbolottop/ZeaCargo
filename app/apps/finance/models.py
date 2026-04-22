from django.db import models


class Payment(models.Model):
    class Method(models.TextChoices):
        CASH = 'cash', 'Наличные'
        CARD = 'card', 'Карта'
        TRANSFER = 'transfer', 'Перевод'

    cargo_company = models.ForeignKey(
        'cargo.CargoCompany',
        on_delete=models.CASCADE,
        related_name='payments',
        verbose_name='Карго-компания'
    )
    client = models.ForeignKey(
        'clients.Client',
        on_delete=models.CASCADE,
        related_name='payments',
        verbose_name='Клиент'
    )
    order = models.ForeignKey(
        'orders.Order',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='payments',
        verbose_name='Заказ'
    )
    amount = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Сумма')
    method = models.CharField(
        max_length=10,
        choices=Method.choices,
        default=Method.CASH,
        verbose_name='Способ оплаты'
    )
    comment = models.TextField(blank=True, verbose_name='Комментарий')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата оплаты')
    created_by = models.ForeignKey(
        'accounts.CustomUser',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Принял'
    )

    class Meta:
        verbose_name = 'Оплата'
        verbose_name_plural = 'Оплаты'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.client.full_name} — {self.amount} ({self.get_method_display()})'
