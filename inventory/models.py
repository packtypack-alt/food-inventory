from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    stock_unit = models.CharField(max_length=100)
    purchase_unit = models.CharField(max_length=100)
    units_per_pack = models.IntegerField()

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class StockCount(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    location = models.ForeignKey(Location, on_delete=models.PROTECT)
    quantity = models.DecimalField(max_digits=9, decimal_places=3)
    counted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product} — {self.location} ({self.quantity})"