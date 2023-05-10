from rest_framework import serializers

class GoodSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=64)
    