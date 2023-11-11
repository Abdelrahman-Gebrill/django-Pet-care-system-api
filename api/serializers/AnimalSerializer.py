from rest_framework import serializers
from ..Model.Animal import Animal

class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = "__all__"
        read_only_fields = ['id']