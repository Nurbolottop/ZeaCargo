from django.db import models
from django.utils.translation import gettext_lazy as _

class CargoCompany(models.Model):
    name = models.CharField(_('Название карго-компании'), max_length=255)
    logo = models.ImageField(_('Логотип'), upload_to='cargo_logos/', blank=True, null=True)
    description = models.TextField(_('Описание'), blank=True)
    contact_phone = models.CharField(_('Контактный телефон'), max_length=50, blank=True)
    contact_telegram = models.CharField(_('Telegram'), max_length=100, blank=True)
    work_schedule = models.CharField(_('Режим работы'), max_length=255, blank=True)
    currency = models.CharField(_('Валюта (короткий код)'), max_length=10, default='USD')
    is_active = models.BooleanField(_('Статус активности'), default=True)
    created_at = models.DateTimeField(_('Дата создания'), auto_now_add=True)

    class Meta:
        verbose_name = _('Карго-компания')
        verbose_name_plural = _('Карго-компании')

    def __str__(self):
        return self.name

class Warehouse(models.Model):
    cargo_company = models.ForeignKey(CargoCompany, on_delete=models.CASCADE, related_name='warehouses', verbose_name=_('Карго-компания'))
    name = models.CharField(_('Название склада'), max_length=255)
    address = models.TextField(_('Адрес'))
    recipient_name = models.CharField(_('Имя получателя'), max_length=255, blank=True)
    recipient_phone = models.CharField(_('Телефон склада'), max_length=50, blank=True)
    instructions = models.TextField(_('Инструкция по заполнению'), blank=True)
    
    class Meta:
        verbose_name = _('Склад')
        verbose_name_plural = _('Склады')

    def __str__(self):
        return f"{self.name} ({self.cargo_company.name})"
