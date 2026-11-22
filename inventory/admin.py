from django.contrib import admin
from .models import Product
from .models import Location

admin.site.register(Product)
admin.site.register(Location)