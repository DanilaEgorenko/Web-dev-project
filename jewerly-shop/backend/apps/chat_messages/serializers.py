from rest_framework import serializers
from django.core.exceptions import ObjectDoesNotExist

from .models import Message
from apps.users.models import User


class MessageSerializer(serializers.Serializer):
    chat_id = serializers.IntegerField()
    user = serializers.CharField()
    text = serializers.CharField()
    
    def validate_user(self, value):
        try:
            User.objects.get(email=value)
            return value
        
        except ObjectDoesNotExist:
            raise serializers.ValidationError("Пользователь {} не найден".format(value))

    def create(self, validated_data):
        chat_id = validated_data['chat_id']
        email = validated_data['user']
        text = validated_data['text']
        user = User.objects.get(email=email)
        
        Message.objects.create(chat_id=chat_id, user=user, text=text)
        
        return self.data
    
    class Meta:
        fields = ["user", "text", "chat_id", ]
