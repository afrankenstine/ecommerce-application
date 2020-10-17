from rest_framework import serializers
from djoser import serializers as djsr
from django.db import transaction

from .models import User, Customer, Seller, Support, Admin
from djoser.conf import settings
from allauth.account.adapter import get_adapter
from dj_rest_auth.registration.serializers import RegisterSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


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
            "seller",
        )


class CustomRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField(max_length=50, allow_blank=True, required=False)
    last_name = serializers.CharField(max_length=50, allow_blank=True, required=False)
    role = serializers.CharField(max_length=50, allow_blank=True, required=False)
    country = serializers.CharField(max_length=200, allow_blank=True, required=False)
    province = serializers.CharField(max_length=50, allow_blank=True, required=False)
    address = serializers.CharField(max_length=300, allow_blank=True, required=False)
    phone_number = serializers.CharField(
        max_length=50, allow_blank=True, required=False
    )
    city = serializers.CharField(max_length=50, allow_blank=True, required=False)
    display_picture = serializers.FileField(
        max_length=None, allow_empty_file=True, required=False
    )

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
            "role",
            "phone_number",
            "display_picture",
            "country",
            "province",
            "city",
            "address",
        )

    def get_cleaned_data(self):
        return {
            "username": self.validated_data.get("username", ""),
            "email": self.validated_data.get("email", ""),
            "password1": self.validated_data.get("password1", ""),
            "password2": self.validated_data.get("password2", ""),
            "first_name": self.validated_data.get("first_name", ""),
            "last_name": self.validated_data.get("last_name", ""),
            "role": self.validated_data.get("role", ""),
            "phone_number": self.validated_data.get("phone_number", ""),
            "city": self.validated_data.get("city", ""),
            "country": self.validated_data.get("country", ""),
            "province": self.validated_data.get("province", ""),
            "address": self.validated_data.get("address", ""),
            "display_picture": self.validated_data.get("display_picture", ""),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        print(self.cleaned_data)
        user.role = self.cleaned_data.get("role")
        user.city = self.cleaned_data.get("city")
        user.phone_number = self.cleaned_data.get("phone_number")
        user.province = self.cleaned_data.get("province")
        user.address = self.cleaned_data.get("address")
        user.country = self.cleaned_data.get("country")
        user.display_picture = self.cleaned_data.get("display_picture")
        user.save()
        adapter.save_user(request, user, self)
        if self.cleaned_data.get("role") == "customer":
            Customer.objects.create(user_id=user)
        elif user.role == "seller":
            Seller.objects.create(user_id=user)
        print(user)
        return user


# class UserRegisterSerializer(djsr.UserCreateSerializer):
#     class Meta:
#         model = User
#         fields = tuple(User.REQUIRED_FIELDS) + (
#             settings.LOGIN_FIELD,
#             settings.USER_ID_FIELD,
#             "password",
#             "first_name",
#             "last_name",
#             "role",
#             "phone_number",
#             "display_picture",
#             "country",
#             "province",
#             "city",
#             "address",
#         )

#     def perform_create(self, validated_data):
#         with transaction.atomic():
#             user = User.objects.create_user(**validated_data)
#             if settings.SEND_ACTIVATION_EMAIL:
#                 user.is_active = False
#                 user.save(update_fields=["is_active"])
#             if user.role == "customer":
#                 Customer.objects.create(user_id=user)
#             elif user.role == "seller":
#                 Seller.objects.create(user_id=user)
#         return user
