from rest_framework import serializers

class GoodSerializer(serializers.Serializer):
    """
    All fields of Goods model that can be accessed from api
    """
    name = serializers.CharField(max_length=64)
    price = serializers.DecimalField(max_digits=9, decimal_places=2)
    category = None
    alloy = serializers.CharField(max_length=64)
    