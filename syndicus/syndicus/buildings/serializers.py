from rest_framework import serializers

from .models import Building, Privative



class PrivativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Privative
        fields = "__all__"
        optional_fields = [
            "owner",
        ]

class BuildingSerializer(serializers.ModelSerializer):
    privatives = PrivativeSerializer(many=True, read_only=True)  # Display related privatives

    class Meta:
        model = Building
        # fields = '__all__'
        exclude = ["id", "created_at", "updated_at"]
