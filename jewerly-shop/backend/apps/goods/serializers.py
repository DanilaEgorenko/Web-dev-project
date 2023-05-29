from rest_framework import serializers


class GoodSerializer(serializers.Serializer):
    """
    All fields of Goods model that can be accessed from api
    """
    title = serializers.CharField(max_length=64)
    price = serializers.DecimalField(max_digits=9, decimal_places=2)
    category = None
    material = serializers.CharField(max_length=64)
    src = serializers.CharField(max_length=9999)
    color = serializers.CharField(max_length=32)
