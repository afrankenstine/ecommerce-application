from rest_framework.routers import DefaultRouter

from .views import (CartItemsView, CartView,
                        WishListItemsView,
                        WishListView)

router = DefaultRouter()
router.register('wishlist', WishListView)
router.register('wishlist-items', WishListItemsView)
router.register('cart', CartView)
router.register('cart-items', CartItemsView)

urlpatterns = router.urls
