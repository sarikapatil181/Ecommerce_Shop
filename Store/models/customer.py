from django.db import models


class Customer(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)
    email=models.EmailField()
    password=models.CharField(max_length=30)

    def register(self):
        self.save()
    def __str__(self):
        return self.first_name
    def get_customer_by_eamil(email):
        try:
            Customer.objects.filter(email=email)
        except:
            return False


    
    def isExist(self):
        if Customer.objects.filter(email=self.email):
            return True
        else:
            return False
