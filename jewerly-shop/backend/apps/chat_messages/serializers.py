from rest_framework import serializers

from .models import Message
from apps.users.models import User


class MessageSerializer(serializers.Serializer):
    chat_id = serializers.IntegerField()
    user = serializers.CharField()
    text = serializers.CharField()

    def create(self, validated_data):
        return self.data
    
    class Meta:
        model = Message
        fields = ["id", "user", "text", "chat_id"]
