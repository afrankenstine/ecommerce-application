from rest_framework.routers import DefaultRouter

from .views import ProductViews, RatingViews, ProductQueryView, ProductQueryAnswerView

router = DefaultRouter()
router.register("product", ProductViews)
router.register("rating", RatingViews)
router.register("query", ProductQueryView)
router.register("query-answer", ProductQueryAnswerView)

urlpatterns = router.urls
