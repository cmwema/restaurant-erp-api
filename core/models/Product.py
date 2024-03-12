import os
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from core.models.Category import Category


def generate_image_filename(instance, filename):
    extension = filename.split('.')[-1]
    
    new_filename = f"product_{instance.id}.{extension}"

    return os.path.join("uploads/products/", new_filename)


class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    description = models.TextField()
    image = models.ImageField(upload_to=generate_image_filename, blank=True, null=True)

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_products()

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Product_detail", kwargs={"pk": self.pk})
    
    def total_orders(self):
        return sum(order_item.quantity for order_item in self.orderitem_set.all())
