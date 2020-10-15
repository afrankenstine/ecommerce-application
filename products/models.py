from django.db import models
from users.models import Seller, User, Customer
from django.db.models import Avg



CATEGORIES = (
    ('men_fashion', (
        ('clothing', 'clothing'),
        ('footwear', 'footwear'),
        ('accessories', 'accessories'),
        ('grooming', 'grooming')
        )
    ),
    ('women_fashion', (
        ('clothing', 'clothing'),
        ('footwear', 'footwear'),
        ('accessories', 'accessories'),
        ('grooming', 'grooming')
        )
    ),
    ('electronics', (
        ('television', 'television'),
        ('smartphones', 'smartphones'),
        ('laptops', 'laptops'),
        ('desktops', 'desktops')
        )
    ),
    ('books',(
        ('fiction', 'fiction'),
        ('nonfiction', 'nonfiction')
        )
    ),
    ('home_decor', (
        ('furniture', 'furniture'),
        ('bedsheets', 'bedsheets')
    ))
)


class Product(models.Model):
    seller = models.ForeignKey(Seller,
        on_delete=models.CASCADE, unique=True)
    name = models.CharField(max_length=50, default='')
    description = models.CharField(max_length=550, default='')
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(
        max_length=15, choices=CATEGORIES, default='customer', null=False, blank=False)

    @property
    def rating(self):
        Rating.objects.filter(product_id=self).aggregate(Avg('rating'))
    
    @property
    def is_availabile(self):
        if self.quantity == 0:
            return False
        else:
            return True


class Rating(models.Model):
    user_id = models.ForeignKey(Customer,
        on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product,
        on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ['user_id', 'product_id']
