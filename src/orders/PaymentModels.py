from django.db import models
from django.conf import settings


class PaymentInformation(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=16, null=True, blank=True)
    expiration_date = models.DateField(null=True, blank=True)
    cvv = models.CharField(max_length=4, null=True, blank=True)
    billing_address = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"PaymentInformation for {self.user.username}"
