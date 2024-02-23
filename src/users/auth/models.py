from django.db import models
from django.utils import timezone
from allauth.account.models import EmailAddress

class Otp(models.Model):
    otp = models.CharField()
    email = models.OneToOneField(EmailAddress,on_delete=models.CASCADE)
    valid_untill = models.DateTimeField()
    
    @property
    def expired(self):
        return self.valid_untill <= timezone.now()