from django.contrib import admin
from .Model.Animal import Animal
from .Model.Food import Food
from .Model.Supplier import Supplier
# from models.User import User
admin.site.register(Animal)
admin.site.register(Food)
admin.site.register(Supplier)
# admin.site.register(Animal)