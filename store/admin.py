from django.contrib import admin
from .models import Product , ProductCategories, ProductImage
# Register your models here.

admin.site.register(ProductCategories)
admin.site.register(Product)
admin.site.register(ProductImage)

