from django.db import models

class Fruit(models.Model):
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} - {self.price} сом"
