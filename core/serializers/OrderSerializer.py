from rest_framework import serializers
from core.models.Order import Order
from core.models.OrderItem import OrderItem


class OrderSerializer(serializers.ModelSerializer):
    order_items = serializers.PrimaryKeyRelatedField(
        queryset=OrderItem.objects.all(),
        many=True,
        required=False
    )

    class Meta:
        model = Order
        fields = '__all__'
