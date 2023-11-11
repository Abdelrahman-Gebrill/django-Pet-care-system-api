from django.shortcuts import render
from rest_framework import viewsets
from .Model.Animal import Animal
from .Model.Food import Food
from .Model.Supplier import Supplier

from .serializers.AnimalSerializer import AnimalSerializer
from .serializers.FoodSerializer import FoodSerializer
from .serializers.SupplierSerializer import SupplierSerializer

# Create your views here.

class AnimalView(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer


class FoodView(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class SupplierView(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer