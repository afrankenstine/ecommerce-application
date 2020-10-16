from django.shortcuts import render
from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.core import exceptions

from .models import Product, Rating

from .serializers import (CartSerializer, CartItemsSerializer, 
                            WishItemsSerializer, WishListSerializer)
from .models import CartItems, Cart, WishList, WishListItems

from users.models import Seller, Customer


class AbstractBaseItemsView(viewsets.GenericViewSet,
                mixins.CreateModelMixin,
                mixins.RetrieveModelMixin,
                mixins.ListModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin):
    
    def create(self, request, *args, **kwargs):
        user = request.user
        data = request.data
        if user.is_authenticated:
            if Customer.objects.get(user_id=user).id == data.get('user'):
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
            if Customer.objects.get(user_id=user).id == int(kwargs['pk']):
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
            if Customer.objects.get(user_id=user).id == int(kwargs['pk']):
                return super().partial_update(request, *args, **kwargs)
            elif user.role == 'support' or 'admin':
                return super().partial_update(request, *args, **kwargs)
            else:
                raise exceptions.PermissionDenied()
        else:
            raise exceptions.PermissionDenied()



class CartItemsView(AbstractBaseItemsView):
    permission_classes = [IsAuthenticated]
    queryset = CartItems.objects.all()
    serializer_class = CartItemsSerializer




class CartView(viewsets.GenericViewSet,
                mixins.CreateModelMixin,
                mixins.RetrieveModelMixin,
                mixins.ListModelMixin,):
    
    permission_classes = [IsAuthenticated]
    queryset = Cart.objects.all()
    serializer_class = CartSerializer



class WishListView(viewsets.GenericViewSet,
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,):
    
    permission_classes = [IsAuthenticated]
    queryset = WishList.objects.all()
    serializer_class = WishListSerializer


class WishListItemsView(AbstractBaseItemsView):    
    permission_classes = [IsAuthenticated]
    queryset = WishListItems.objects.all()
    serializer_class = WishItemsSerializer
