from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from users.permissions import IsManagerUser

from core.serializers.ProductSerializer import ProductSerializer
from core.serializers.OrderItemSerializer import OrderItemSerializer
from core.serializers.CategorySerializer import CategorySerializer
from core.serializers.OrderSerializer import OrderSerializer
from core.serializers.table import TableSerializer
from core.serializers.Reviewserializer import ReviewSerializer

from core.models.Product import Product
from core.models.OrderItem import OrderItem
from core.models.Order import Order
from core.models.Category import Category
from core.models.table import Table
from core.models.review import Review

class ReviewView(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class TableView(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    permission_classes = [IsAuthenticatedOrReadOnly | IsManagerUser]


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsAuthenticatedOrReadOnly | IsManagerUser]


class OrderItemView(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer



class OrderView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_destroy(self, instance):
        order_items = OrderItem.objects.filter(order=instance)
        order_items.delete()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    permission_classes = [IsAuthenticatedOrReadOnly | IsManagerUser]
