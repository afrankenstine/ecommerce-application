from django.db import models


from users.models import Customer
from products.models import Product
from cart.models import Cart

class Invoice(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
