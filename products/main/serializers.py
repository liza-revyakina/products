from rest_framework import serializers
from .models import Review, Product


class ReviewSerializer(serializers.ModelSerializer):
    # реализуйте все поля
    class Meta:
        model = Review
        fields = "__all__"
    pass


class ProductListSerializer(serializers.Serializer):
    # реализуйте поля title и price
    title = serializers.CharField(max_length=100)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    pass


class ProductDetailsSerializer(serializers.ModelSerializer):
    # реализуйте поля title, description, price и reviews (список отзывов к товару)
    comments = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ["title", "description", "price", "comments"]
    pass
