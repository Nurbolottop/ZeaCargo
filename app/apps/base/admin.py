from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import HomePageSettings, SiteSettings


class SingletonAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not self.model.objects.exists()

    def changelist_view(self, request, extra_context=None):
        obj = self.model.load()
        return HttpResponseRedirect(
            reverse(
                f"admin:{self.model._meta.app_label}_{self.model._meta.model_name}_change",
                args=[obj.pk],
            )
        )


@admin.register(SiteSettings)
class SiteSettingsAdmin(SingletonAdmin):
    fieldsets = (
        ("Основное", {"fields": ("site_name", "logo_image", "logo_emoji")}),
        ("SEO", {"fields": ("meta_title", "meta_description")}),
        ("Футер и контакты", {"fields": ("footer_about", "footer_copyright", "telegram_url", "whatsapp_url", "instagram_url")}),
    )


@admin.register(HomePageSettings)
class HomePageSettingsAdmin(SingletonAdmin):
    fieldsets = (
        ("Hero", {"fields": ("badge_text", "hero_title", "hero_highlight", "hero_description")}),
        ("Кнопки Hero", {"fields": ("hero_primary_text", "hero_primary_url", "hero_secondary_text", "hero_secondary_url")}),
        (
            "Статистика",
            {
                "fields": (
                    "stats_companies_value",
                    "stats_companies_label",
                    "stats_clients_value",
                    "stats_clients_label",
                    "stats_orders_value",
                    "stats_orders_label",
                    "stats_uptime_value",
                    "stats_uptime_label",
                )
            },
        ),
        ("CTA", {"fields": ("cta_title", "cta_description", "cta_primary_text", "cta_primary_url", "cta_secondary_text", "cta_secondary_url")}),
    )