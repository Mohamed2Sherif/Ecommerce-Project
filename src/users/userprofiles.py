from src.address.models import Address
from django.conf import settings
from src.orders.models import Order
from src.products.models import Product
from django.db import models

class PaymentInformation(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=16, null=True, blank=True)
    expiration_date = models.DateField(null=True, blank=True)
    cvv = models.CharField(max_length=4, null=True, blank=True)
    billing_address = models.TextField(null=True, blank=True)
    
    
    def __str__(self):
        return f"PaymentInformation for {self.user.username}"

    #FIXME: Create a save method right here and perforom hashing for all card information
    #before saving any info to the database.
    
class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    profilePicture = models.ImageField(upload_to="Customerimages/")
    paymentInformation = models.OneToOneField(PaymentInformation, null=True,blank=True,on_delete=models.SET_NULL)
    address = models.OneToOneField(Address,on_delete=models.CASCADE)
class Vendor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    
    #business information
    company_name = models.CharField(max_length=255)
    business_registration_id = models.CharField(max_length=50)
    tax_id = models.CharField(max_length=20)
    
    # store contact information
    company_email = models.EmailField()
    company_phone_number = models.CharField(max_length=15)
    
    # Payment and Invoicing
    payment_history = models.TextField()
    invoices = models.TextField()
    
    #store and brand information
    store_description = models.TextField()
    store_policies = models.TextField()
    