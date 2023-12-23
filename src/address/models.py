from django.db import models
import uuid
from src.users.models import User

class AddressTypeChoices(models.TextChoices):
    BILLING = 'billing', 'Billing'
    HOME = 'home', 'Home'
    OFFICE = 'office', 'Office'
# Create your models here.
class Address(models.Model):
    address_ID = models.UUIDField(primary_key=True,db_index=True,unique=True,)
    user_ID = models.ForeignKey(User,on_delete=models.CASCADE,db_index = True)
    effective_Date = models.DateField()
    address_type = models.CharField(max_length=20, choices=AddressTypeChoices.choices)
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)

    class Meta:
        indexes = [
            models.Index(fields=['user']),
            models.Index(fields=['effective_date']),
            models.Index(fields=['address_type']),
            models.Index(fields=['country']),
            models.Index(fields=['zip_code']),
        ]

    def __str__(self):
        return f"{self.address_type} Address for {self.user.username}"