from django.db import models
from core.models.Product import Product

RATINGS = [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
]


class Review(models.Model):
    comment = models.TextField()
    rating = models.IntegerField(choices=RATINGS)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
