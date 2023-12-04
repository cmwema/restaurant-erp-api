from rest_framework import serializers
from core.models.Product import Product


class ProductSerializer(serializers.ModelSerializer):
    image_url = serializers.ImageField(required=False)
    total_orders = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = "__all__"

    def get_total_orders(self, obj):
        return obj.total_orders
