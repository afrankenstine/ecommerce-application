from django.urls import path
from .views import VerifyKhaltiPayment

urlpatterns = [
    path("verifypayment/khalti/", VerifyKhaltiPayment.as_view()),
]
