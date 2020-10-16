from rest_framework import serializers

from .models import CartItems, Cart, WishList, WishListItems


class CartItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItems
        fields = "__all__"


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"


class WishItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishListItems
        fields = "__all__"


class WishListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishList
        fields = "__all__"
