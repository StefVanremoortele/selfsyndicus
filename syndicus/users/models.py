import uuid

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager as BUM
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from syndicus.common.models import BaseModel

# Taken from here:
# https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#a-full-example
# With some modifications


class BaseUserManager(BUM):
    def create_user(self, email, is_active=True, is_admin=False, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email.lower()),
            is_active=is_active,
            is_admin=is_admin,
        )

        if password is not None:
            user.set_password(password)
        else:
            user.set_unusable_password()

        user.full_clean()
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email=email,
            is_active=True,
            is_admin=True,
            password=password,
        )

        user.is_superuser = True
        user.save(using=self._db)

        return user


class BaseUser(BaseModel, AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    # This should potentially be an encrypted field
    jwt_key = models.UUIDField(default=uuid.uuid4)

    objects = BaseUserManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email

    def is_staff(self):
        return self.is_admin


# class Tenant(BaseModel, AbstractBaseUser, PermissionsMixin):
#     pass

# class Supplier(BaseModel, AbstractBaseUser, PermissionsMixin):
#     pass


class Supplier(BaseUser):
    company_name = models.CharField(max_length=255)
    address = models.CharField(max_length=500, blank=True, null=True)
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    tax_number = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"Supplier: {self.company_name} ({self.email})"


# class Customer(BaseUser):
#     full_name = models.CharField(max_length=255)
#     address = models.CharField(max_length=500)
#     phone_number = models.CharField(max_length=15)
#     date_of_birth = models.DateField()
#     preferred_contact_method = models.CharField(
#         choices=[("email", "Email"), ("phone", "Phone")], max_length=5
#     )

#     def __str__(self):
#         return f"Customer: {self.full_name} ({self.email})"
