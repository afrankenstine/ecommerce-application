from rest_framework import serializers
from djoser import serializers as djsr
from django.db import transaction

from .models import User, Customer, Seller, Support, Admin
from djoser.conf import settings


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserViewSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)
    seller = SellerSerializer(read_only=True)
    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "role",
            "phone_number",
            "display_picture",
            "country",
            "province",
            "city",
            "address",
            "customer",
            "seller",)

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"

class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = "__all__"

class SupportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Support
        fields = "__all__"


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = "__all__"


class UserViewSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    seller = SellerSerializer()
    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "role",
            "phone_number",
            "display_picture",
            "country",
            "province",
            "city",
            "address",
            "customer",
            "seller",)


class UserRegisterSerializer(djsr.UserCreateSerializer):
    class Meta:
        model = User
        fields = tuple(User.REQUIRED_FIELDS) + (
            settings.LOGIN_FIELD,
            settings.USER_ID_FIELD,
            "password",
            "role",
            "phone_number",
            "display_picture",
            "country",
            "province",
            "city",
            "address",
        )

    def perform_create(self, validated_data):
        with transaction.atomic():
            user = User.objects.create_user(**validated_data)
            if settings.SEND_ACTIVATION_EMAIL:
                user.is_active = False
                user.save(update_fields=["is_active"])
            if user.role == "customer":
                Customer.objects.create(user_id=user)
            elif user.role == "seller":
                Seller.objects.create(user_id=user) 
        return user