from rest_framework import serializers

from .models import Product, Rating, ProductQuery, ProductQueryAnswers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = "__all__"


class ProductQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductQuery
        fields = "__all__"


class ProductQueryAnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductQueryAnswers
        fields = "__all__"
