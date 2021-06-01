from django.db import models
from .category import Category
class Product(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField(default=0)
    description=models.CharField(max_length=200,default='')
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    image=models.ImageField(upload_to='Uploads/products/')
    def __str__(self):
        return self.name
    

    @staticmethod
    def get_all_products():
        return Product.objects.all()
    def get_products_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.objects.all()

