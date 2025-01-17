from rest_framework import serializers

from syndicus.privatives.models import Privative



class PrivativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Privative
        fields = "__all__"
        optional_fields = [
            "owner",
        ]
