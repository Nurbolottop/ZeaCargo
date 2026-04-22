from django.db import models
from django_resized import ResizedImageField


class Product(models.Model):
    class Category(models.TextChoices):
        CLOTHES = 'clothes', 'Одежда'
        SHOES = 'shoes', 'Обувь'
        ACCESSORIES = 'accessories', 'Аксессуары'
        ELECTRONICS = 'electronics', 'Электроника'
        HOME = 'home', 'Товары для дома'
        COSMETICS = 'cosmetics', 'Косметика'
        AUTO = 'auto', 'Автотовары'
        KIDS = 'kids', 'Детские товары'
        OTHER = 'other', 'Другое'

    cargo_company = models.ForeignKey(
        'cargo.CargoCompany',
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name='Карго-компания'
    )
    name = models.CharField(max_length=300, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    category = models.CharField(
        max_length=20,
        choices=Category.choices,
        default=Category.OTHER,
        verbose_name='Категория'
    )
    article = models.CharField(max_length=100, blank=True, verbose_name='Артикул')
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Цена')
    original_link = models.URLField(blank=True, verbose_name='Ссылка на оригинал')
    image = ResizedImageField(
        size=[800, 800],
        quality=85,
        upload_to='catalog/products/',
        null=True,
        blank=True,
        force_format='WEBP',
        verbose_name='Фото'
    )
    is_available = models.BooleanField(default=True, verbose_name='В наличии')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-created_at']

    def __str__(self):
        return self.name


class PurchaseRequest(models.Model):
    class Status(models.TextChoices):
        NEW = 'new', 'Новая'
        REVIEWING = 'reviewing', 'На рассмотрении'
        WAITING_CONFIRM = 'waiting_confirm', 'Ожидает подтверждения'
        CONFIRMED = 'confirmed', 'Подтверждена'
        REJECTED = 'rejected', 'Отклонена'
        PURCHASED = 'purchased', 'Выкуплена'
        SHIPPED = 'shipped', 'Передана в доставку'

    client = models.ForeignKey(
        'clients.Client',
        on_delete=models.CASCADE,
        related_name='purchase_requests',
        verbose_name='Клиент'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='requests',
        verbose_name='Товар'
    )
    link = models.URLField(blank=True, verbose_name='Ссылка на товар')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')
    size = models.CharField(max_length=50, blank=True, verbose_name='Размер')
    color = models.CharField(max_length=100, blank=True, verbose_name='Цвет')
    comment = models.TextField(blank=True, verbose_name='Комментарий')
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.NEW,
        verbose_name='Статус'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата заявки')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')

    class Meta:
        verbose_name = 'Заявка на выкуп'
        verbose_name_plural = 'Заявки на выкуп'
        ordering = ['-created_at']

    def __str__(self):
        return f'Заявка #{self.pk} — {self.client.full_name}'
