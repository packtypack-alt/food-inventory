from django.contrib import admin
from .models import Product
from .models import Location
from .models import StockCount

admin.site.register(Product)
admin.site.register(Location)
admin.site.register(StockCount)