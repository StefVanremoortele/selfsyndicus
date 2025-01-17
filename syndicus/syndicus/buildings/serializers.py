from rest_framework import serializers

from syndicus.privatives.serializers import PrivativeSerializer

from .models import Building



# class PrivativeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Privative
#         fields = "__all__"
#         optional_fields = [
#             "owner",
#         ]

class BuildingSerializer(serializers.ModelSerializer):
    privatives = PrivativeSerializer(many=True, read_only=True)  # Display related privatives

    class Meta:
        model = Building
        # fields = '__all__'
        exclude = ["created_at", "updated_at"]
