from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField(blank = False,null=False)
    quanitity = models.PositiveIntegerField(blank = False,null=False)
    description = models.TextField(blank = False,null=False)
    guide = models.TextField(blank = False,null=False)
    picture = models.ImageField(upload_to ="Products",blank = False,null=False)
    type = models.CharField(max_length=200)

    class Meta:
        abstract = True