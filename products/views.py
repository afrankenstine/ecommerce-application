from django.shortcuts import render
from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.core import exceptions

from .models import Product, Rating
from .serializers import ProductSerializer, RatingSerializer

from users.models import Seller


class ProductViews(viewsets.GenericViewSet,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.CreateModelMixin,
                    mixins.UpdateModelMixin):
    permission_classes = [AllowAny]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        user = request.user
        data = request.data
        if user.is_authenticated:
            if Seller.objects.get(user_id=user).id == data.get('seller'):
                return super().create(request, *args, **kwargs)
            elif user.role == 'support' or 'admin':
                return super().create(request, *args, **kwargs)
            else:
                raise exceptions.PermissionDenied()
        else:
            raise exceptions.PermissionDenied()

    def update(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            if Seller.objects.get(user_id=user).id == int(kwargs['pk']):
                return super().update(request, *args, **kwargs)
            elif user.role == 'support' or 'admin':
                return super().update(request, *args, **kwargs)
            else:
                raise exceptions.PermissionDenied()
        else:
            raise exceptions.PermissionDenied()

    def partial_update(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            if Seller.objects.get(user_id=user).id == int(kwargs['pk']):
                return super().partial_update(request, *args, **kwargs)
            elif user.role == 'support' or 'admin':
                return super().partial_update(request, *args, **kwargs)
            else:
                raise exceptions.PermissionDenied()
        else:
            raise exceptions.PermissionDenied()


class RatingViews(viewsets.GenericViewSet,
                mixins.ListModelMixin,
                mixins.RetrieveModelMixin,
                mixins.CreateModelMixin,
                mixins.UpdateModelMixin):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = self.queryset.all()
        user = self.request.user
        queryset = queryset.filter(user=user)
        return queryset
    
    def retrieve(self, request, *args, **kwargs):
        user = request.user
        requested_user = int(kwargs['pk'])
        if Rating.objects.get(user=requested_user) == 'seller':
            return super().retrieve(request, *args, **kwargs)
        else:
            raise exceptions.PermissionDenied()
