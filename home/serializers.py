from rest_framework import serializers
from .models import Car


class CarSerializr(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"
