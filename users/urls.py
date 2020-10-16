from rest_framework.routers import DefaultRouter

from .views import UserProfileViews, SellerViews

router = DefaultRouter()
router.register("user-profile", UserProfileViews)
router.register("seller", SellerViews)


urlpatterns = router.urls
