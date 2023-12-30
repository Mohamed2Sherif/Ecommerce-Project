from django.contrib import admin
from .models import User


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["email", "username", "User_ID"]
    list_filter = ["email", "username", "Last_Name", "is_superuser"]
    search_fields = ["email", "username", "First_Name"]
    date_hierarchy = "Created"
    ordering = ["is_active", "email"]
