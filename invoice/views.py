from django.conf import settings
from rest_framework.views import APIView
import requests
from rest_framework.response import Response
import json
from .models import Invoice
from users.models import Customer


class VerifyKhaltiPayment(APIView):
    def post(self, request, *args, **kwargs):
        token = request.POST.get("token")
        amount = request.POST.get("amount")
        url = settings.KHALTI_VERIFY_URL
        secret_key = settings.KHALTI_SECRET_KEY
        payload = {
            "token": token,
            "amount": amount,
        }
        headers = {"Authorization": f"Key {secret_key}"}
        try:
            response = requests.post(url, payload, headers=headers)
            if response.status_code == 200:
                data = json.loads(response.json())
                Invoice.objects.create(
                    payment_amount=data["amount"],
                    fee_amount=data["fee_amount"],
                    transaction_user=data["user"]["name"],
                    transaction_user_idx=data["user"]["idx"],
                    transaction_user_mobile=data["user"]["mobile"],
                    payment_id=request.data.get("payment"),
                    customer=Customer.objects.get(user_id=request.user),
                )
                return Response(
                    {
                        "status": True,
                        "details": response.json(),
                    }
                )

            else:
                return Response(
                    {
                        "status": False,
                        "details": response.json(),
                    }
                )

        except requests.exceptions.HTTPError as exception:
            return Response(
                {
                    "status": False,
                    "details": response.json(),
                }
            )
