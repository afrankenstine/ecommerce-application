from django.db import models


from users.models import Customer, Seller
from products.models import Product
from cart.models import Cart

class Invoice(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    payment_amount = models.IntegerField(default=0)
    customer = models.ForeignKey(Customer,
        on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart,
        on_delete=models.CASCADE)
    
