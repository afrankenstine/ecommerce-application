from django.contrib import admin
from .models import Invoice, Payment, PaymentItems

admin.site.register(Invoice)
admin.site.register(Payment)
admin.site.register(PaymentItems)
# Register your models here.
