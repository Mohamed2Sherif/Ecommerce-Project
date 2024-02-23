from django.contrib import admin
from .models import User
from .auth.models import Otp

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["email", "username", "id"]
    list_filter = ["email", "username", "last_name", "is_superuser"]
    search_fields = ["email", "username", "first_name"]
    date_hierarchy = "created"
    ordering = ["is_active", "email"]



# Register your models here.
@admin.register(Otp)
class OtpAdmin(admin.ModelAdmin):
    list_display = ["email","valid_untill"]