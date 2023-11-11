from rest_framework import serializers
from ..Model.Food import Food

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = "__all__"
        read_only_fields = ['id']