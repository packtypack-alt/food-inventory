from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    stock_unit = models.CharField(max_length=100)
    purchase_unit = models.CharField(max_length=100)
    units_per_pack = models.IntegerField()

    def __str__(self):
        return self.name

class Location(models.Model):
    point_in = models.CharField(max_length=100)

    def __str__(self):
        return self.point_in