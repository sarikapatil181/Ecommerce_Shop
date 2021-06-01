from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer

class adminProduct(admin.ModelAdmin):
    list_display=['name','price','category']
# Register your models here.
admin.site.register(Product,adminProduct)
admin.site.register(Category)
admin.site.register(Customer)