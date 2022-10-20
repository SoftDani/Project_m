from rest_framework import serializers
from .models import Product


# LIST
class ProductListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name', 'creation_date')


# DETAIL
class ProductDetailSerializer(serializers.ModelSerializer):
    creation_date = serializers.ReadOnlyField()

    class Meta:
        model = Product
        fields = "__all__"
