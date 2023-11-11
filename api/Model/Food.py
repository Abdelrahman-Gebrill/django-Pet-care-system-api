from .Product import Product
from django.db import models
class Food(Product):
    size = models.CharField(max_length=100,blank=False,null=False)
    
    def __str__(self):
        return self.name