from django.contrib import admin
from .models import Product, Rating, ProductQuery, ProductQueryAnswers

admin.site.register(Product)
admin.site.register(Rating)
admin.site.register(ProductQuery)
admin.site.register(ProductQueryAnswers)
# Register your models here.
