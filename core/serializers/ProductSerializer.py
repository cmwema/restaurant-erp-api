from rest_framework import serializers
from core.models.Product import Product

class ProductSerializer(serializers.ModelSerializer):
    image_url = serializers.ImageField(required=False)
    
    class Meta:
        model = Product
        fields = '__all__'