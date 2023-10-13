from django.db import models
from core.models.OrderItem import OrderItem
from core.models.table import Table

ORDER_TYPE = (
    ("eat_in", "Eat In"),
    ("take_away", "Take Away"),
    ("delivery", "Delivery"),
)


class Order(models.Model):
    order_type = models.CharField(max_length=20, choices=ORDER_TYPE, default="eat_in")
    order_items = models.ManyToManyField(OrderItem, through="OrderItemAssociation")
    table = models.ManyToManyField(Table, blank=True)

    class Meta:
        ordering = ["order_type"]

    def __str__(self):
        return f"Order {self.pk} ({self.get_order_type_display()})"

    def add_item(self, item, quantity=1):
        order_item_association, created = OrderItemAssociation.objects.get_or_create(
            order=self, item=item
        )
        if not created:
            order_item_association.quantity += quantity
            order_item_association.save()

    def remove_item(self, item, quantity=1):
        try:
            order_item_association = OrderItemAssociation.objects.get(
                order=self, item=item
            )
            if order_item_association.quantity > quantity:
                order_item_association.quantity -= quantity
                order_item_association.save()
            else:
                order_item_association.delete()
        except OrderItemAssociation.DoesNotExist:
            pass

    def get_total_price(self):
        total_price = 0
        for association in self.orderitemassociation_set.all():
            total_price += association.item.price * association.quantity
        return total_price


class OrderItemAssociation(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(OrderItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
