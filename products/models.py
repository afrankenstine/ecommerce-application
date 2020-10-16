from django.db import models
from users.models import Seller, User, Customer
from django.db.models import Avg
import os
from django.utils.timezone import now


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


def upload_pic_to(instance, filename):
     filename_base, filename_ext = os.path.splitext(filename)
     return f'ProductData/product_pics/{now().strftime("%Y%m%d")+filename_ext}'


class Product(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default='')
    description = models.CharField(max_length=550, default='')
    photo1 = models.FileField(upload_to=upload_pic_to, default='', blank=True)
    photo2 = models.FileField(upload_to=upload_pic_to, default='', blank=True)
    photo3 = models.FileField(upload_to=upload_pic_to, default='', blank=True)
    photo4 = models.FileField(upload_to=upload_pic_to, default='', blank=True)
    photo5 = models.FileField(upload_to=upload_pic_to, default='', blank=True)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    ratings = models.ManyToManyField(Customer, blank=True, through="Rating")
    category = models.CharField(
        max_length=15, choices=CATEGORIES, default='customer')

    @property
    def avg_rating(self):
        Rating.objects.filter(product_id=self).aggregate(Avg('rating'))
    
    @property
    def is_availabile(self):
        if self.quantity == 0:
            return False
        else:
            return True


class Rating(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ['user', 'product']
