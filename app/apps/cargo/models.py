from django.db import models
from django_resized import ResizedImageField


class CargoCompany(models.Model):
    class Currency(models.TextChoices):
        KGS = 'KGS', 'Сом (KGS)'
        RUB = 'RUB', 'Рубль (RUB)'
        KZT = 'KZT', 'Тенге (KZT)'
        USD = 'USD', 'Доллар (USD)'

    name = models.CharField(max_length=200, verbose_name='Название')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='Slug (URL)')
    logo = ResizedImageField(
        size=[200, 200],
        quality=90,
        upload_to='cargo/logos/',
        null=True,
        blank=True,
        force_format='WEBP',
        verbose_name='Логотип'
    )
    description = models.TextField(blank=True, verbose_name='Описание')

    # Контакты
    phone = models.CharField(max_length=50, blank=True, verbose_name='Телефон')
    telegram = models.CharField(max_length=100, blank=True, verbose_name='Telegram')
    whatsapp = models.CharField(max_length=50, blank=True, verbose_name='WhatsApp')
    address = models.TextField(blank=True, verbose_name='Адрес склада')
    working_hours = models.CharField(max_length=200, blank=True, verbose_name='Режим работы')

    # Настройки
    currency = models.CharField(
        max_length=3,
        choices=Currency.choices,
        default=Currency.KGS,
        verbose_name='Валюта'
    )

    # Telegram-бот
    bot_token = models.CharField(
        max_length=200,
        blank=True,
        verbose_name='Токен Telegram-бота'
    )

    # Статус
    is_active = models.BooleanField(default=True, verbose_name='Активна')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = 'Карго-компания'
        verbose_name_plural = 'Карго-компании'
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def get_managers_count(self):
        return self.managers.filter(is_active=True).count()

    def get_clients_count(self):
        return self.clients.filter(is_active=True).count()

    def get_active_orders_count(self):
        return self.orders.exclude(
            delivery_status='issued'
        ).count()
