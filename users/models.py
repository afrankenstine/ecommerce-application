from django.db import models
from django.contrib.auth.models import AbstractUser
import os
from django.utils.timezone import now


ROLES = (
    ("customer", "customer"),
    ("seller", "seller"),
    ("support", "support"),
    ("admin", "admin"),
)


def upload_dp_to(instance, filename):
    filename_base, filename_ext = os.path.splitext(filename)
    return f'UserData/display_picture/{now().strftime("%Y%m%d")+filename_ext}'


class User(AbstractUser):
    email = models.EmailField(max_length=70, unique=True)
    phone_number = models.CharField(max_length=15, default="")
    display_picture = models.FileField(upload_to=upload_dp_to, default="", blank=True)
    role = models.CharField(
        max_length=15, choices=ROLES, default="customer", null=False, blank=False
    )
    country = models.CharField(max_length=50, default="")
    province = models.CharField(max_length=50, default="")
    city = models.CharField(max_length=50, default="")
    address = models.CharField(max_length=50, default="")
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    @property
    def is_customer(self):
        if self.role:
            if self.role == "customer":
                return True
        return False

    @property
    def is_seller(self):
        if self.role:
            if self.role == "seller":
                return True
        return False

    @property
    def is_support(self):
        if self.role:
            if self.role == "support":
                return True
        return False

    @property
    def is_admin(self):
        if self.role:
            if self.role == "admin":
                return True
        return False


class Customer(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)


class Seller(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)


class Support(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)


class Admin(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
