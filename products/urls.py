from rest_framework.routers import DefaultRouter

from .views import ProductViews, RatingViews

router = DefaultRouter()
router.register("product", ProductViews)
router.register("rating", RatingViews)


urlpatterns = router.urls
