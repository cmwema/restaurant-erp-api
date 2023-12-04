from rest_framework import serializers
from core.models.Order import Order
from core.models.OrderItem import OrderItem
from core.models.table import Table


class OrderSerializer(serializers.ModelSerializer):
    order_items = serializers.PrimaryKeyRelatedField(
        queryset=OrderItem.objects.all(), many=True, required=False
    )
    table = serializers.PrimaryKeyRelatedField(
        queryset=Table.objects.all(), many=True, required=False
    )

    class Meta:
        model = Order
        fields = "__all__"
