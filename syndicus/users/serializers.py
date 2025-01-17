from rest_framework import serializers

from .models import BaseUser


class BaseUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = BaseUser
        fields = "__all__"
        # exclude = ["created_at", "updated_at"]
