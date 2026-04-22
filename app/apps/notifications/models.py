from django.db import models


class Notification(models.Model):
    class Channel(models.TextChoices):
        TELEGRAM = 'telegram', 'Telegram'
        SMS = 'sms', 'SMS'

    class Status(models.TextChoices):
        PENDING = 'pending', 'Ожидает'
        SENT = 'sent', 'Отправлено'
        FAILED = 'failed', 'Ошибка'

    client = models.ForeignKey(
        'clients.Client',
        on_delete=models.CASCADE,
        related_name='notifications',
        verbose_name='Клиент'
    )
    order = models.ForeignKey(
        'orders.Order',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='notifications',
        verbose_name='Заказ'
    )
    channel = models.CharField(
        max_length=10,
        choices=Channel.choices,
        default=Channel.TELEGRAM,
        verbose_name='Канал'
    )
    message = models.TextField(verbose_name='Текст уведомления')
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.PENDING,
        verbose_name='Статус'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    sent_at = models.DateTimeField(null=True, blank=True, verbose_name='Дата отправки')
    error_message = models.TextField(blank=True, verbose_name='Ошибка')

    class Meta:
        verbose_name = 'Уведомление'
        verbose_name_plural = 'Уведомления'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.client.full_name} — {self.get_channel_display()} — {self.get_status_display()}'
