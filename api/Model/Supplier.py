from .Product import Product
from django.db import models
class Supplier(Product):
    size = models.CharField(max_length=100,blank=False,null=False)
    color = models.CharField(max_length=100,blank=False,null=False)
    
    def __str__(self):
        return self.name