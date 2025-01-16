from rest_framework import serializers
from .models import Building, Privative

class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        # fields = '__all__'
        exclude = ['id', 'created_at', 'updated_at']
    
    # created_at = serializers.DateTimeField(read_only=True)


class PrivativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Privative
        fields = '__all__'
