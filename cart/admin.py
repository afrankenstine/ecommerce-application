from django.contrib import admin
from .models import CartItems, Cart, WishList, WishListItems

admin.site.register(Cart)
admin.site.register(CartItems)
admin.site.register(WishList)
admin.site.register(WishListItems)
# Register your models here.
