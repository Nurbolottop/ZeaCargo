from django.contrib import admin
from .models import CargoCompany


@admin.register(CargoCompany)
class CargoCompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'currency', 'is_active', 'get_managers_count', 'created_at')
    list_filter = ('is_active', 'currency')
    search_fields = ('name', 'slug', 'phone', 'telegram')
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Основное', {
            'fields': ('name', 'slug', 'logo', 'description', 'is_active')
        }),
        ('Контакты', {
            'fields': ('phone', 'telegram', 'whatsapp', 'address', 'working_hours')
        }),
        ('Настройки', {
            'fields': ('currency', 'bot_token')
        }),
        ('Системное', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
