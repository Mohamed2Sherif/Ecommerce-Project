from django.contrib import admin
from .models import Address


# Register your models here.
@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "address_type",
        "effective_date",
        "address_line_1",
        "city",
        "country",
        "zip_code",
    ]
    list_filter = ["address_type", "city", "country"]
    search_fields = ["user__username", "address_line_1", "city", "country", "zip_code"]
    date_hierarchy = "effective_date"
    ordering = ["city", "country", "effective_date"]

    #  Customize the detail view
    fieldsets = [
        ("User Information", {"fields": ["user"]}),
        (
            "Address Details",
            {
                "fields": [
                    "address_type",
                    "effective_date",
                    "address_line_1",
                    "address_line_2",
                    "city",
                    "country",
                    "zip_code",
                ]
            },
        ),
    ]

    #  Add readonly_fields if needed
    # readonly_fields = ['user']
