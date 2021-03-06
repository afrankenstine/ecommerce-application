from django.db import models
from users.models import Seller, User, Customer
from django.db.models import Avg
import os
from django.utils.timezone import now
from django.conf import settings


CATEGORIES = (
    (
        "men_fashion",
        (
            ("clothing", "clothing"),
            ("footwear", "footwear"),
            ("accessories", "accessories"),
            ("grooming", "grooming"),
        ),
    ),
    (
        "women_fashion",
        (
            ("clothing", "clothing"),
            ("footwear", "footwear"),
            ("accessories", "accessories"),
            ("grooming", "grooming"),
        ),
    ),
    (
        "electronics",
        (
            ("television", "television"),
            ("smartphones", "smartphones"),
            ("laptops", "laptops"),
            ("desktops", "desktops"),
        ),
    ),
    ("books", (("fiction", "fiction"), ("nonfiction", "nonfiction"))),
    ("home_decor", (("furniture", "furniture"), ("bedsheets", "bedsheets"))),
)


def upload_pic_to(instance, filename):
    filename_base, filename_ext = os.path.splitext(filename)
    return f'{settings.MEDIA_ROOT}/ProductData/product_pics/{now().strftime("%Y%m%d")+filename_ext}'


class Product(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default="")
    description = models.CharField(max_length=550, default="")
    photo1 = models.FileField(upload_to=upload_pic_to, default="", blank=True)
    photo2 = models.FileField(upload_to=upload_pic_to, default="", blank=True)
    photo3 = models.FileField(upload_to=upload_pic_to, default="", blank=True)
    photo4 = models.FileField(upload_to=upload_pic_to, default="", blank=True)
    photo5 = models.FileField(upload_to=upload_pic_to, default="", blank=True)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # users_ratings = models.ManyToManyField(
    #     "Rating", blank=True, related_name="product_user_ratings"
    # )  # through="Rating")
    # users_queries = models.ManyToManyField(
    #     "ProductQuery", blank=True, related_name="product_user_queries"
    # )  # through="ProductQuery")
    category = models.CharField(max_length=15, choices=CATEGORIES, default="")

    def __str__(self):
        return self.name

    @property
    def avg_rating(self):
        return Rating.objects.filter(product_id=self).aggregate(Avg("rating"))

    @property
    def is_available(self):
        if self.quantity == 0:
            return False
        else:
            return True


class Rating(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    review = models.CharField(max_length=550, default="")
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ["user", "product"]


class ProductQuery(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    query = models.CharField(max_length=250, default="")
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.query


class ProductQueryAnswers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    answer = models.CharField(max_length=550, default="")
    parent = models.ForeignKey(ProductQuery, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


# class Replies(models.Model):
#     user = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     question = models.CharField(max_length=250, default='')
#     updated_at = models.DateTimeField(auto_now=True)
#     created_at = models.DateTimeField(auto_now_add=True)
