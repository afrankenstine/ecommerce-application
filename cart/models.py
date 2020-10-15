from django.db import models

from users.models import Customer
from products.models import Product


class Cart(models.Model):
    user = models.OneToOneField(Customer,
        on_delete=models.CASCADE)
    items = models.ManyToManyField(Product, through='CartItems')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CartItems(models.Model):
    user = models.ForeignKey(Customer,
        on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart,
        on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Order(models.Model):
    user_id = models.ForeignKey(Customer,
        on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product,
        on_delete=models.CASCADE)
    ordered_at = models.DateTimeField(auto_now_add=True)
    