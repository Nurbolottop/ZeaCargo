from django.db import models


class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class SiteSettings(SingletonModel):
    site_name = models.CharField("Название сайта", max_length=120, default="ZeaCargo")
    meta_title = models.CharField(
        "SEO title",
        max_length=255,
        default="ZeaCargo — Платформа для карго-компаний",
    )
    meta_description = models.TextField(
        "SEO описание",
        default="ZeaCargo — единая SaaS-платформа для карго-компаний. CRM, Telegram-бот, каталог товаров и аналитика в одной системе.",
    )
    logo_image = models.ImageField("Логотип", upload_to="site/", blank=True, null=True)
    logo_emoji = models.CharField("Эмодзи логотипа", max_length=10, default="📦")
    footer_about = models.TextField(
        "Текст в футере",
        default="Единая SaaS-платформа для карго-компаний. Автоматизируйте доставку, учёт и коммуникацию с клиентами.",
    )
    footer_copyright = models.CharField(
        "Копирайт",
        max_length=255,
        default="© 2025 ZeaCargo. Все права защищены.",
    )
    telegram_url = models.URLField("Telegram ссылка", blank=True)
    whatsapp_url = models.URLField("WhatsApp ссылка", blank=True)
    instagram_url = models.URLField("Instagram ссылка", blank=True)

    class Meta:
        verbose_name = "Настройки сайта"
        verbose_name_plural = "Настройки сайта"
        db_table = "cms_sitesettings"

    def __str__(self):
        return self.site_name


class HomePageSettings(SingletonModel):
    badge_text = models.CharField(
        "Текст бейджа",
        max_length=255,
        default="🚀 Новая версия 2.0 уже доступна",
    )
    hero_title = models.CharField("Заголовок главной", max_length=255, default="Единая платформа")
    hero_highlight = models.CharField(
        "Выделенный текст заголовка",
        max_length=255,
        default="карго-компаний",
    )
    hero_description = models.TextField(
        "Описание главной",
        default="CRM, Telegram-бот, каталог товаров и финансовый учёт в одной системе. Автоматизируйте доставку из Китая и управляйте своим бизнесом легко.",
    )
    hero_primary_text = models.CharField("Текст основной кнопки", max_length=120, default="Попробовать бесплатно")
    hero_primary_url = models.CharField("Ссылка основной кнопки", max_length=255, default="/auth/login.html")
    hero_secondary_text = models.CharField("Текст второй кнопки", max_length=120, default="Узнать больше ↓")
    hero_secondary_url = models.CharField("Ссылка второй кнопки", max_length=255, default="#features")
    stats_companies_value = models.CharField("Статистика 1: значение", max_length=50, default="500+")
    stats_companies_label = models.CharField("Статистика 1: подпись", max_length=120, default="Карго-компаний")
    stats_clients_value = models.CharField("Статистика 2: значение", max_length=50, default="12K+")
    stats_clients_label = models.CharField("Статистика 2: подпись", max_length=120, default="Клиентов")
    stats_orders_value = models.CharField("Статистика 3: значение", max_length=50, default="85K+")
    stats_orders_label = models.CharField("Статистика 3: подпись", max_length=120, default="Заказов в месяц")
    stats_uptime_value = models.CharField("Статистика 4: значение", max_length=50, default="99.9%")
    stats_uptime_label = models.CharField("Статистика 4: подпись", max_length=120, default="Аптайм")
    cta_title = models.CharField("Заголовок CTA", max_length=255, default="Готовы автоматизировать своё карго?")
    cta_description = models.TextField(
        "Описание CTA",
        default="Попробуйте платформу бесплатно — войдите в демо-кабинет прямо сейчас",
    )
    cta_primary_text = models.CharField("CTA кнопка 1 текст", max_length=120, default="Открыть демо →")
    cta_primary_url = models.CharField("CTA кнопка 1 ссылка", max_length=255, default="/auth/login.html")
    cta_secondary_text = models.CharField("CTA кнопка 2 текст", max_length=120, default="Смотреть CRM")
    cta_secondary_url = models.CharField("CTA кнопка 2 ссылка", max_length=255, default="/auth/login.html")

    class Meta:
        verbose_name = "Настройки главной страницы"
        verbose_name_plural = "Настройки главной страницы"
        db_table = "cms_homepagesettings"

    def __str__(self):
        return "Главная страница"
