from django.db import models
from django.contrib.auth.models import AbstractUser
import os
from django.utils.timezone import now


ROLES = (
    ('customer', 'CUSTOMER'),
    ('seller', 'SELLER'),
    ('support','SUPPORT'),
    ('admin', 'ADMIN')
)

def upload_dp_to(instance, filename):
     filename_base, filename_ext = os.path.splitext(filename)
     return f'UserData/photo/{now().strftime("%Y%m%d")+filename_ext}'


class User(AbstractUser):
    display_picture = models.FileField(upload_to=upload_dp_to, default='')
    role = models.CharField(
        max_length=15, choices=ROLES, default='customer', null=False, blank=False)
    country = models.CharField(max_length=50, default='')
    province = models.CharField(max_length=50, default='')
    city = models.CharField(max_length=50, default='')
    address = models.CharField(max_length=50, default='')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'



