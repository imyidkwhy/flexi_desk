from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Spot, Booking, CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'phone_number', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number',)}),
    )


class SpotAdmin(admin.ModelAdmin):
    list_display = ("title", "floor", "cabinet", "status")
    prepopulated_fields = {"slug": ("title", )}


class BookingAdmin(admin.ModelAdmin):
    list_display = ("customer", "spot", "date")


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Spot, SpotAdmin)
admin.site.register(Booking, BookingAdmin)
