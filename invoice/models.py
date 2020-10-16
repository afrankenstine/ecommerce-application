from django.db import models
from users.models import Customer, Seller
from products.models import Product
from cart.models import Cart


PAYMENT_STATUS = (("paid", "paid"), ("unpaid", "unpaid"))


class Invoice(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    payment_amount = models.IntegerField(default=0)
    fee_amount = models.IntegerField(default=0)
    payment_id = models.ForeignKey("Payment", on_delete=models.SET_NULL)
    transaction_user = models.CharField(max_length=50, default="")
    transaction_user_idx = models.CharField(max_length=50, default="")
    transaction_user_mobile = models.CharField(max_length=50, default="")
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL)


class Payment(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    items = models.ManyToManyField(Product, blank=True, through="PaymentItems")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=15, choices=PAYMENT_STATUS, default="unpaid")


class PaymentItems(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)