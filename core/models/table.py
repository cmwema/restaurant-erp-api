from django.db import models

class Table(models.Model):
    capacity = models.IntegerField()

    def __str__(self) -> str:
        return f'Table {self.id}'