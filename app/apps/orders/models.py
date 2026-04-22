from django.db import models


class Group(models.Model):
    """Группа (партия) заказов — отправляется одним рейсом."""
    cargo_company = models.ForeignKey(
        'cargo.CargoCompany',
        on_delete=models.CASCADE,
        related_name='groups',
        verbose_name='Карго-компания'
    )
    name = models.CharField(max_length=200, verbose_name='Название группы')
    description = models.TextField(blank=True, verbose_name='Описание')
    departure_date = models.DateField(null=True, blank=True, verbose_name='Дата отправки')
    arrival_date = models.DateField(null=True, blank=True, verbose_name='Ожидаемая дата прибытия')
    is_active = models.BooleanField(default=True, verbose_name='Активна')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} ({self.cargo_company.name})'


class Order(models.Model):
    class DeliveryStatus(models.TextChoices):
        WAITING = 'waiting', 'Ожидается на складе'
        ACCEPTED = 'accepted', 'Принят на складе'
        PREPARING = 'preparing', 'Подготовлен к отправке'
        IN_TRANSIT = 'in_transit', 'В пути'
        ARRIVED = 'arrived', 'Прибыл в страну'
        SORTING = 'sorting', 'На сортировке'
        READY = 'ready', 'Готов к выдаче'
        ISSUED = 'issued', 'Выдан клиенту'
        PROBLEM = 'problem', 'Проблема / Возврат'

    class PaymentStatus(models.TextChoices):
        UNPAID = 'unpaid', 'Не оплачен'
        PARTIAL = 'partial', 'Частично оплачен'
        PAID = 'paid', 'Полностью оплачен'

    cargo_company = models.ForeignKey(
        'cargo.CargoCompany',
        on_delete=models.CASCADE,
        related_name='orders',
        verbose_name='Карго-компания'
    )
    client = models.ForeignKey(
        'clients.Client',
        on_delete=models.CASCADE,
        related_name='orders',
        verbose_name='Клиент'
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='orders',
        verbose_name='Группа'
    )

    # Идентификация
    track_number = models.CharField(max_length=100, verbose_name='Трек-номер')
    internal_number = models.CharField(max_length=50, blank=True, verbose_name='Внутренний номер')
    shop = models.CharField(max_length=200, blank=True, verbose_name='Магазин')
    description = models.TextField(blank=True, verbose_name='Описание товара')

    # Логистика
    weight = models.DecimalField(
        max_digits=8, decimal_places=3,
        null=True, blank=True,
        verbose_name='Вес (кг)'
    )
    price_per_kg = models.DecimalField(
        max_digits=10, decimal_places=2,
        null=True, blank=True,
        verbose_name='Цена за кг'
    )
    total_price = models.DecimalField(
        max_digits=12, decimal_places=2,
        null=True, blank=True,
        verbose_name='Итоговая стоимость'
    )

    # Статусы
    delivery_status = models.CharField(
        max_length=20,
        choices=DeliveryStatus.choices,
        default=DeliveryStatus.WAITING,
        verbose_name='Статус доставки'
    )
    payment_status = models.CharField(
        max_length=10,
        choices=PaymentStatus.choices,
        default=PaymentStatus.UNPAID,
        verbose_name='Статус оплаты'
    )

    comment = models.TextField(blank=True, verbose_name='Комментарий оператора')

    # Даты
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    sent_at = models.DateField(null=True, blank=True, verbose_name='Дата отправки')
    arrived_at = models.DateField(null=True, blank=True, verbose_name='Дата прибытия')
    issued_at = models.DateField(null=True, blank=True, verbose_name='Дата выдачи')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.track_number} — {self.client.full_name}'

    def save(self, *args, **kwargs):
        # Автоматически считаем итог если есть вес и цена
        if self.weight and self.price_per_kg:
            self.total_price = self.weight * self.price_per_kg
        super().save(*args, **kwargs)
