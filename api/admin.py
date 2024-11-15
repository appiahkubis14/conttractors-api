from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Contractor, Farmer
from django.utils.html import format_html

# Registering the Contractor model with custom UserAdmin configuration
@admin.register(Contractor)
class ContractorAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('full_name',)
        }
    ),
)
    list_display = ['username', 'full_name', 'email', 'is_staff']
    search_fields = ['username', 'full_name', 'email']

# Registering the Farmer model
class FarmerAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'date_of_birth', 'gender', 'contact_number', 'email', 'address','photo_display']
    search_fields = ['full_name', 'email', 'contact_number']
    list_filter = ['gender']

    def photo_display(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="50" height="50" />', obj.photo.url)
        return "No Photo"

    photo_display.short_description = 'Photo'

admin.site.register(Farmer, FarmerAdmin)
