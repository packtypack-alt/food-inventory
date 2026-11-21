from django.db import models
from dataclasses import dataclass

@dataclass
class Product(moldels.Model):
    name = models.CharField(max_length=100)
    unit_of_remaining_stock = models.CharField(max_length=100)
    purchasing_unit = models.CharField(max_length=100)
    units_per_pack = models.IntegerField()

    def __str__(self):
        return self.name