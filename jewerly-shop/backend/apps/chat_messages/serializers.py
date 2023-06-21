from rest_framework import serializers
from django.core.exceptions import ObjectDoesNotExist

from .models import Message
from apps.users.models import User


class ChatSerializer(serializers.Serializer):
    email = serializers.CharField()
    text = serializers.CharField()
    
    def validate_user(self, value):
        try:
            user = User.objects.get(email=value)
            return user.id
        
        except ObjectDoesNotExist:
            raise serializers.ValidationError("Пользователь {} не найден".format(value))
        
    def validate(self, attrs):
        return attrs

    # def create(self, validated_data):
    #     return self.data
