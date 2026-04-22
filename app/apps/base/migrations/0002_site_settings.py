from django.db import migrations, models


CREATE_SITE_SETTINGS_SQL = """
CREATE TABLE IF NOT EXISTS cms_sitesettings (
    id bigint PRIMARY KEY,
    site_name varchar(120) NOT NULL,
    meta_title varchar(255) NOT NULL,
    meta_description text NOT NULL,
    logo_image varchar(100) NULL,
    logo_emoji varchar(10) NOT NULL,
    footer_about text NOT NULL,
    footer_copyright varchar(255) NOT NULL,
    telegram_url varchar(200) NOT NULL,
    whatsapp_url varchar(200) NOT NULL,
    instagram_url varchar(200) NOT NULL
);
"""

CREATE_HOMEPAGE_SETTINGS_SQL = """
CREATE TABLE IF NOT EXISTS cms_homepagesettings (
    id bigint PRIMARY KEY,
    badge_text varchar(255) NOT NULL,
    hero_title varchar(255) NOT NULL,
    hero_highlight varchar(255) NOT NULL,
    hero_description text NOT NULL,
    hero_primary_text varchar(120) NOT NULL,
    hero_primary_url varchar(255) NOT NULL,
    hero_secondary_text varchar(120) NOT NULL,
    hero_secondary_url varchar(255) NOT NULL,
    stats_companies_value varchar(50) NOT NULL,
    stats_companies_label varchar(120) NOT NULL,
    stats_clients_value varchar(50) NOT NULL,
    stats_clients_label varchar(120) NOT NULL,
    stats_orders_value varchar(50) NOT NULL,
    stats_orders_label varchar(120) NOT NULL,
    stats_uptime_value varchar(50) NOT NULL,
    stats_uptime_label varchar(120) NOT NULL,
    cta_title varchar(255) NOT NULL,
    cta_description text NOT NULL,
    cta_primary_text varchar(120) NOT NULL,
    cta_primary_url varchar(255) NOT NULL,
    cta_secondary_text varchar(120) NOT NULL,
    cta_secondary_url varchar(255) NOT NULL
);
"""


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0001_initial"),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[
                migrations.RunSQL(CREATE_SITE_SETTINGS_SQL, reverse_sql="DROP TABLE IF EXISTS cms_sitesettings;"),
                migrations.RunSQL(CREATE_HOMEPAGE_SETTINGS_SQL, reverse_sql="DROP TABLE IF EXISTS cms_homepagesettings;"),
            ],
            state_operations=[
                migrations.CreateModel(
                    name="SiteSettings",
                    fields=[
                        ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                        ("site_name", models.CharField(default="ZeaCargo", max_length=120, verbose_name="Название сайта")),
                        ("meta_title", models.CharField(default="ZeaCargo — Платформа для карго-компаний", max_length=255, verbose_name="SEO title")),
                        ("meta_description", models.TextField(default="ZeaCargo — единая SaaS-платформа для карго-компаний. CRM, Telegram-бот, каталог товаров и аналитика в одной системе.", verbose_name="SEO описание")),
                        ("logo_image", models.ImageField(blank=True, null=True, upload_to="site/", verbose_name="Логотип")),
                        ("logo_emoji", models.CharField(default="📦", max_length=10, verbose_name="Эмодзи логотипа")),
                        ("footer_about", models.TextField(default="Единая SaaS-платформа для карго-компаний. Автоматизируйте доставку, учёт и коммуникацию с клиентами.", verbose_name="Текст в футере")),
                        ("footer_copyright", models.CharField(default="© 2025 ZeaCargo. Все права защищены.", max_length=255, verbose_name="Копирайт")),
                        ("telegram_url", models.URLField(blank=True, verbose_name="Telegram ссылка")),
                        ("whatsapp_url", models.URLField(blank=True, verbose_name="WhatsApp ссылка")),
                        ("instagram_url", models.URLField(blank=True, verbose_name="Instagram ссылка")),
                    ],
                    options={
                        "verbose_name": "Настройки сайта",
                        "verbose_name_plural": "Настройки сайта",
                        "db_table": "cms_sitesettings",
                    },
                ),
                migrations.CreateModel(
                    name="HomePageSettings",
                    fields=[
                        ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                        ("badge_text", models.CharField(default="🚀 Новая версия 2.0 уже доступна", max_length=255, verbose_name="Текст бейджа")),
                        ("hero_title", models.CharField(default="Единая платформа", max_length=255, verbose_name="Заголовок главной")),
                        ("hero_highlight", models.CharField(default="карго-компаний", max_length=255, verbose_name="Выделенный текст заголовка")),
                        ("hero_description", models.TextField(default="CRM, Telegram-бот, каталог товаров и финансовый учёт в одной системе. Автоматизируйте доставку из Китая и управляйте своим бизнесом легко.", verbose_name="Описание главной")),
                        ("hero_primary_text", models.CharField(default="Попробовать бесплатно", max_length=120, verbose_name="Текст основной кнопки")),
                        ("hero_primary_url", models.CharField(default="/auth/login.html", max_length=255, verbose_name="Ссылка основной кнопки")),
                        ("hero_secondary_text", models.CharField(default="Узнать больше ↓", max_length=120, verbose_name="Текст второй кнопки")),
                        ("hero_secondary_url", models.CharField(default="#features", max_length=255, verbose_name="Ссылка второй кнопки")),
                        ("stats_companies_value", models.CharField(default="500+", max_length=50, verbose_name="Статистика 1: значение")),
                        ("stats_companies_label", models.CharField(default="Карго-компаний", max_length=120, verbose_name="Статистика 1: подпись")),
                        ("stats_clients_value", models.CharField(default="12K+", max_length=50, verbose_name="Статистика 2: значение")),
                        ("stats_clients_label", models.CharField(default="Клиентов", max_length=120, verbose_name="Статистика 2: подпись")),
                        ("stats_orders_value", models.CharField(default="85K+", max_length=50, verbose_name="Статистика 3: значение")),
                        ("stats_orders_label", models.CharField(default="Заказов в месяц", max_length=120, verbose_name="Статистика 3: подпись")),
                        ("stats_uptime_value", models.CharField(default="99.9%", max_length=50, verbose_name="Статистика 4: значение")),
                        ("stats_uptime_label", models.CharField(default="Аптайм", max_length=120, verbose_name="Статистика 4: подпись")),
                        ("cta_title", models.CharField(default="Готовы автоматизировать своё карго?", max_length=255, verbose_name="Заголовок CTA")),
                        ("cta_description", models.TextField(default="Попробуйте платформу бесплатно — войдите в демо-кабинет прямо сейчас", verbose_name="Описание CTA")),
                        ("cta_primary_text", models.CharField(default="Открыть демо →", max_length=120, verbose_name="CTA кнопка 1 текст")),
                        ("cta_primary_url", models.CharField(default="/auth/login.html", max_length=255, verbose_name="CTA кнопка 1 ссылка")),
                        ("cta_secondary_text", models.CharField(default="Смотреть CRM", max_length=120, verbose_name="CTA кнопка 2 текст")),
                        ("cta_secondary_url", models.CharField(default="/auth/login.html", max_length=255, verbose_name="CTA кнопка 2 ссылка")),
                    ],
                    options={
                        "verbose_name": "Настройки главной страницы",
                        "verbose_name_plural": "Настройки главной страницы",
                        "db_table": "cms_homepagesettings",
                    },
                ),
            ],
        ),
    ]
