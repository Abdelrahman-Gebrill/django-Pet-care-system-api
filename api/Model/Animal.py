from .Product import Product
from django.db import models
class Animal(Product):
    color = models.CharField(max_length=100,blank=False,null=False)
    age = models.PositiveIntegerField(blank=False,null=False)

    def __str__(self):
        return self.name