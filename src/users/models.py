from django.db import models
import uuid
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404


class UserManager(BaseUserManager):
    def get_user(self, public_id):
        try:
            instance = self.get(user_id=public_id)
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
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, db_index=True, unique=True, editable=False
    )
    username = models.CharField(db_index=True, max_length=25)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(
        unique=True,
        db_index=True,
    )
    created = models.DateTimeField(auto_now_add=True)
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
