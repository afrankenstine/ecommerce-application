from django.shortcuts import render
from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.core import exceptions

from .models import Product, Rating, ProductQuery, ProductQueryAnswers
from .serializers import (
    ProductSerializer,
    RatingSerializer,
    ProductQuerySerializer,
    ProductQueryAnswersSerializer,
)

from users.models import Seller, Customer
from notification.signals import notify


class ProductViews(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
):
    permission_classes = [AllowAny]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        user = request.user
        data = request.data
        if user.is_authenticated:
            if Seller.objects.get(user_id=user).id == data.get("seller"):
                return super().create(request, *args, **kwargs)
            elif user.role == "support" or user.role == "admin":
                return super().create(request, *args, **kwargs)
            else:
                raise exceptions.PermissionDenied()
        else:
            raise exceptions.PermissionDenied()

    def update(self, request, *args, **kwargs):
        user = request.user
        requested_product = int(kwargs["pk"])
        if user.is_authenticated:
            if (
                Seller.objects.get(user_id=user)
                == Product.objects.get(id=requested_product).seller
            ):
                return super().update(request, *args, **kwargs)
            elif user.role == "support" or user.role == "admin":
                return super().update(request, *args, **kwargs)
            else:
                raise exceptions.PermissionDenied()
        else:
            raise exceptions.PermissionDenied()

    def partial_update(self, request, *args, **kwargs):
        user = request.user
        requested_product = int(kwargs["pk"])
        if user.is_authenticated:
            if (
                Seller.objects.get(user_id=user)
                == Product.objects.get(id=requested_product).seller
            ):
                return super().partial_update(request, *args, **kwargs)
            elif user.role == "support" or user.role == "admin":
                return super().partial_update(request, *args, **kwargs)
            else:
                raise exceptions.PermissionDenied()
        else:
            raise exceptions.PermissionDenied()


class RatingViews(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
):
    permission_classes = [IsAuthenticated]
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    def get_queryset(self):
        queryset = self.queryset.all()
        user = self.request.user
        print("I got till here")
        return queryset

    def retrieve(self, request, *args, **kwargs):
        user = request.user
        requested_rating = int(kwargs["pk"])
        if Rating.objects.get(id=requested_rating).user == Customer.object.get(
            user_id=user
        ):
            return super().retrieve(request, *args, **kwargs)
        else:
            raise exceptions.PermissionDenied()

    def create(self, request, *args, **kwargs):
        user = request.user
        data = request.data
        if user.is_authenticated and user.role == "customer":
            if Customer.objects.get(user_id=user).id == data.get("user"):
                product = data.get("product")
                product_item = Product.objects.get(id=product)
                seller = product_item.seller.user_id
                description = f"You have a new Rating for your product {product_item}."
                notify.send(sender=None, recipient=seller, description=description)
                return super().create(request, *args, **kwargs)
            elif user.role == "support" or user.role == "admin":
                return super().create(request, *args, **kwargs)
            else:
                raise exceptions.PermissionDenied()
        else:
            raise exceptions.PermissionDenied()

    def update(self, request, *args, **kwargs):
        user = request.user
        requested_rating = int(kwargs["pk"])
        if user.is_authenticated and user.role == "customer":
            if (
                Customer.objects.get(user_id=user)
                == Rating.objects.get(id=requested_rating).user
            ):
                return super().update(request, *args, **kwargs)
            elif user.role == "support" or user.role == "admin":
                return super().update(request, *args, **kwargs)
            else:
                raise exceptions.PermissionDenied()
        else:
            raise exceptions.PermissionDenied()

    def partial_update(self, request, *args, **kwargs):
        user = request.user
        requested_rating = int(kwargs["pk"])
        if user.is_authenticated and user.role == "customer":
            if (
                Customer.objects.get(user_id=user)
                == Rating.objects.get(id=requested_rating).user
            ):
                return super().partial_update(request, *args, **kwargs)
            elif user.role == "support" or user.role == "admin":
                return super().partial_update(request, *args, **kwargs)
            else:
                raise exceptions.PermissionDenied()
        else:
            raise exceptions.PermissionDenied()


class ProductQueryView(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
):
    permission_classes = [IsAuthenticated]
    queryset = ProductQuery.objects.all()
    serializer_class = ProductQuerySerializer

    def create(self, request, *args, **kwargs):
        user = request.user
        data = request.data
        if user.is_authenticated:
            if user.id == int(data.get("user")):
                product = data.get("product")
                product_item = Product.objects.get(id=product)
                seller = product_item.seller.user_id
                description = f"You have a new Question for the {product_item}."
                notify.send(sender=None, recipient=seller, description=description)
                return super().create(request, *args, **kwargs)
            elif user.role == "support" or user.role == "admin":
                return super().create(request, *args, **kwargs)
            else:
                raise exceptions.PermissionDenied()
        else:
            raise exceptions.PermissionDenied()

    def update(self, request, *args, **kwargs):
        user = request.user
        requested_query = int(kwargs["pk"])
        if user.is_authenticated:
            if user == ProductQuery.objects.get(id=requested_query).user:
                return super().update(request, *args, **kwargs)
            elif user.role == "support" or user.role == "admin":
                return super().update(request, *args, **kwargs)
            else:
                raise exceptions.PermissionDenied()
        else:
            raise exceptions.PermissionDenied()

    def partial_update(self, request, *args, **kwargs):
        user = request.user
        requested_query = int(kwargs["pk"])
        if user.is_authenticated:
            if user == ProductQuery.objects.get(id=requested_query).user:
                return super().partial_update(request, *args, **kwargs)
            elif user.role == "support" or user.role == "admin":
                return super().partial_update(request, *args, **kwargs)
            else:
                raise exceptions.PermissionDenied()
        else:
            raise exceptions.PermissionDenied()


class ProductQueryAnswerView(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
):
    permission_classes = [IsAuthenticated]
    queryset = ProductQueryAnswers.objects.all()
    serializer_class = ProductQueryAnswersSerializer

    def create(self, request, *args, **kwargs):
        user = request.user
        data = request.data
        if user.is_authenticated:
            if user.id == data.get("user"):
                product = data.get("product")
                product_item = Product.objects.get(id=product)
                seller = product_item.seller.user_id
                description = f"You have a new Answer for your product {product_item}."
                notify.send(sender=None, recipient=seller, description=description)
                reply_to = data.get("parent")
                query = ProductQuery.objects.get(id=reply_to)
                user = query.user
                description = f'You have a new Answer for you question "{query}" on the product "{product_item}".'
                notify.send(sender=None, recipient=user, description=description)
                return super().create(request, *args, **kwargs)
            elif user.role == "support" or user.role == "admin":
                return super().create(request, *args, **kwargs)
            else:
                raise exceptions.PermissionDenied()
        else:
            raise exceptions.PermissionDenied()

    def update(self, request, *args, **kwargs):
        user = request.user
        requested_query = int(kwargs["pk"])
        if user.is_authenticated:
            if user == ProductQuery.objects.get(id=requested_query).user:
                return super().update(request, *args, **kwargs)
            elif user.role == "support" or user.role == "admin":
                return super().update(request, *args, **kwargs)
            else:
                raise exceptions.PermissionDenied()
        else:
            raise exceptions.PermissionDenied()

    def partial_update(self, request, *args, **kwargs):
        user = request.user
        requested_query = int(kwargs["pk"])
        if user.is_authenticated:
            if user == ProductQuery.objects.get(id=requested_query).user:
                return super().partial_update(request, *args, **kwargs)
            elif user.role == "support" or user.role == "admin":
                return super().partial_update(request, *args, **kwargs)
            else:
                raise exceptions.PermissionDenied()
        else:
            raise exceptions.PermissionDenied()
