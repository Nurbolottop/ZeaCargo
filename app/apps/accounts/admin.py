from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'get_full_name', 'role', 'cargo_company', 'is_active')
    list_filter = ('role', 'cargo_company', 'is_active')
    search_fields = ('username', 'email', 'first_name', 'last_name', 'phone')
    ordering = ('-date_joined',)

    fieldsets = UserAdmin.fieldsets + (
        ('ZeaCargo', {
            'fields': ('role', 'cargo_company', 'phone', 'avatar'),
        }),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('ZeaCargo', {
            'fields': ('role', 'cargo_company', 'phone'),
        }),
    )
