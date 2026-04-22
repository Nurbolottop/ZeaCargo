from django.contrib import admin
from .models import CargoCompany, Warehouse

@admin.register(CargoCompany)
class CargoCompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_phone', 'currency', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('name', 'contact_phone', 'contact_telegram')

@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'cargo_company', 'recipient_name')
    list_filter = ('cargo_company',)
    search_fields = ('name', 'address')
