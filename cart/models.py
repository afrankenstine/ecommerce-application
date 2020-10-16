from django.db import models

from users.models import Customer
from products.models import Product


CART_STATUS = (("paid", "paid"), ("unpaid", "unpaid"))

WISH_STATUS = (("purchased", "purchased"), ("remaining", "remaining"))


class BaseListModel(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class BaseItemsModel(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Cart(BaseListModel):
    items = models.ManyToManyField(Product, blank=True, through="CartItems")
    # status = models.CharField(max_length=15,
    #     choices=CART_STATUS, default='unpaid')


class CartItems(BaseItemsModel):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    cart_quantity = models.IntegerField(default=1)
    status = models.CharField(max_length=15, choices=CART_STATUS, default="unpaid")


class WishList(BaseListModel):
    items = models.ManyToManyField(Product, blank=True, through="WishListItems")
    # status = models.CharField(max_length=15,
    #     choices=WISH_STATUS, default='remaining')


class WishListItems(BaseItemsModel):
    wish_list = models.ForeignKey(WishList, on_delete=models.CASCADE)
    status = models.CharField(max_length=15, choices=WISH_STATUS, default="remaining")


# class Order(models.Model):
#     user_id = models.ForeignKey(Customer,
#         on_delete=models.CASCADE)
#     product_id = models.ForeignKey(Product,
#         on_delete=models.CASCADE)
#     ordered_at = models.DateTimeField(auto_now_add=True)
