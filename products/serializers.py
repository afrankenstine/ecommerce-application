from rest_framework import serializers

from .models import Product, Rating, ProductQuery, ProductQueryAnswers


class ProductSerializer(serializers.ModelSerializer):
    avg_rating = serializers.ReadOnlyField()
    is_available = serializers.ReadOnlyField()

    class Meta:
        model = Product
        fields = "__all__"
        # [
        #     "seller",
        #     "name",
        #     "description",
        #     "photo1",
        #     "photo2",
        #     "photo3",
        #     "photo4",
        #     "photo5",
        #     "price",
        #     "quantity",
        #     "updated_at",
        #     "created_at",
        #     "ratings",
        #     "queries",
        #     "category",
        #     "avg_rating",
        #     "is_available",
        # ]  # + ["avg_rating", "is_availabe"]


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
