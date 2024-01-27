from django.db import models
import uuid
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

from django.contrib.auth import get_user_model
from src.orders.models import Order
from src.products.models import Product


class UserManager(BaseUserManager):
    def get_user(self, public_id):
        try:
            instance = self.get(User_ID=public_id)
            return instance
        except (ObjectDoesNotExist, ValueError, TypeError):
            return Http404

    def create_user(self, email, username, password=None, *args, **kwargs):
        if email is None:
            raise TypeError("Please provide an email address")
        if username is None:
            raise TypeError("Please provide a username")
        if password is None:
            raise TypeError("Please provide a password")

        user = self.model(
            username=username, email=self.normalize_email(email), **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, username, password=None, **kwargs):
        if email is None:
            raise TypeError("Please provide an email address")
        if username is None:
            raise TypeError("Please provide a username")
        if password is None:
            raise TypeError("Please provide a password")

        user = self.create_user(email, username, password, **kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    User_ID = models.UUIDField(
        primary_key=True, default=uuid.uuid4, db_index=True, unique=True, editable=False
    )
    username = models.CharField(db_index=True, max_length=25)
    First_Name = models.CharField(max_length=25)
    Last_Name = models.CharField(max_length=25)
    email = models.EmailField(
        unique=True,
        db_index=True,
    )
    Created = models.DateTimeField(auto_now_add=True)
    verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.username

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"

    # TODO: Create the save method for user model and hash the important user fields

from src.address.models import Address
class PaymentInformation(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    card_number = models.CharField(max_length=16, null=True, blank=True)
    expiration_date = models.DateField(null=True, blank=True)
    cvv = models.CharField(max_length=4, null=True, blank=True)
    billing_address = models.TextField(null=True, blank=True)
    
    
    def __str__(self):
        return f"PaymentInformation for {self.user.username}"

    #FIXME: Create a save method right here and perforom hashing for all card information
    #before saving any info to the database.
    
class Customer(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete= models.CASCADE)
    profilePicture = models.ImageField(upload_to="Customerimages/")
    paymentInformation = models.OneToOneField(PaymentInformation, null=True,blank=True,on_delete=models.SET_NULL)
    address = models.OneToOneField(Address,on_delete=models.CASCADE)
class Vendor(models.Model):
    user = models.OneToOneField(get_user_model(),on_delete=models.CASCADE)
    
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
    