from django.db import models
from users.models import Seller, User, Customer

class Product(models.Model):
    seller = models.OneToOneField(Seller,
        on_delete=models.CASCADE, unique=True)
    name = models.CharField(max_length=50, default='')
    description = models.CharField(max_length=550, default='')
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)


class Rating(models.Model):
    user_id = models.OneToOneField(Customer,
        on_delete=models.CASCADE)
    product_id = models.OneToOneField(Product,
        on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    class Meta:
        unique_together = ['user_id', 'product_id']
