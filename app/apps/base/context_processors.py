
from types import SimpleNamespace

from django.db.utils import OperationalError, ProgrammingError

from .models import HomePageSettings, SiteSettings


DEFAULT_SITE_SETTINGS = SimpleNamespace(
    site_name="ZeaCargo",
    meta_title="ZeaCargo — Платформа для карго-компаний",
    meta_description="ZeaCargo — единая SaaS-платформа для карго-компаний. CRM, Telegram-бот, каталог товаров и аналитика в одной системе.",
    logo_image=None,
    logo_emoji="📦",
    footer_about="Единая SaaS-платформа для карго-компаний. Автоматизируйте доставку, учёт и коммуникацию с клиентами.",
    footer_copyright="© 2025 ZeaCargo. Все права защищены.",
    telegram_url="",
    whatsapp_url="",
    instagram_url="",
)

DEFAULT_HOMEPAGE_SETTINGS = SimpleNamespace(
    badge_text="🚀 Новая версия 2.0 уже доступна",
    hero_title="Единая платформа",
    hero_highlight="карго-компаний",
    hero_description="CRM, Telegram-бот, каталог товаров и финансовый учёт в одной системе. Автоматизируйте доставку из Китая и управляйте своим бизнесом легко.",
    hero_primary_text="Попробовать бесплатно",
    hero_primary_url="/auth/login.html",
    hero_secondary_text="Узнать больше ↓",
    hero_secondary_url="#features",
    stats_companies_value="500+",
    stats_companies_label="Карго-компаний",
    stats_clients_value="12K+",
    stats_clients_label="Клиентов",
    stats_orders_value="85K+",
    stats_orders_label="Заказов в месяц",
    stats_uptime_value="99.9%",
    stats_uptime_label="Аптайм",
    cta_title="Готовы автоматизировать своё карго?",
    cta_description="Попробуйте платформу бесплатно — войдите в демо-кабинет прямо сейчас",
    cta_primary_text="Открыть демо →",
    cta_primary_url="/auth/login.html",
    cta_secondary_text="Смотреть CRM",
    cta_secondary_url="/auth/login.html",
)


def site_settings_context(request):
    try:
        site_settings = SiteSettings.load()
        homepage_settings = HomePageSettings.load()
    except (OperationalError, ProgrammingError):
        site_settings = DEFAULT_SITE_SETTINGS
        homepage_settings = DEFAULT_HOMEPAGE_SETTINGS

    return {
        "site_settings": site_settings,
        "homepage_settings": homepage_settings,
    }
