from django.contrib import admin
from .models import User, Customer, Seller, Support, Admin


admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Seller)
admin.site.register(Support)
admin.site.register(Admin)
# Register your models here.
