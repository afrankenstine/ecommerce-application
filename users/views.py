from django.shortcuts import render
from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.core import exceptions

from .serializers import UserViewSerializer, CustomerSerializer, SellerSerializer

from .models import Customer, User, Seller


class UserProfileViews(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
):

    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserViewSerializer

    def get_queryset(self):
        queryset = self.queryset.all()
        user = self.request.user
        if user.is_authenticated:
            queryset = queryset.filter(id=user.id)
            return queryset
        else:
            raise exceptions.PermissionDenied()

    def retrieve(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            if user.id == int(kwargs["pk"]):
                return super().retrieve(request, *args, **kwargs)
            elif user.role == "support" or "admin":
                return super().retrieve(request, *args, **kwargs)
            else:
                raise exceptions.PermissionDenied()
        else:
            raise exceptions.PermissionDenied()

    def update(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            if user.id == int(kwargs["pk"]):
                return super().update(request, *args, **kwargs)
            elif user.role == "support" or "admin":
                return super().update(request, *args, **kwargs)
            else:
                raise exceptions.PermissionDenied()
        else:
            raise exceptions.PermissionDenied()

    def partial_update(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            if user.id == int(kwargs["pk"]):
                return super().partial_update(request, *args, **kwargs)
            elif user.role == "support" or "admin":
                return super().partial_update(request, *args, **kwargs)
            else:
                raise exceptions.PermissionDenied()
        else:
            raise exceptions.PermissionDenied()


class SellerViews(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
):

    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserViewSerializer

    def get_queryset(self):
        queryset = self.queryset.all()
        # user = self.request.user
        queryset = queryset.filter(role="seller")
        return queryset

    def retrieve(self, request, *args, **kwargs):
        user = request.user
        requested_user = int(kwargs["pk"])
        if User.objects.get(id=requested_user).role == "seller":
            return super().retrieve(request, *args, **kwargs)
        else:
            raise exceptions.PermissionDenied()
