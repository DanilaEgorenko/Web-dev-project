from rest_framework import serializers

from apps.orders.models import Order


class OrderSerializer(serializers.Serializer):
    user_id = serializers.CharField()

    class Meta:
        model = Order
        fields = ["id", "user_id", "goods_list"]


class GetOrderSerializer(serializers.Serializer):
    user_id = serializers.CharField()

    class Meta:
        model = Order
        fields = ["id", "user_id", "goods_list"]
        
class CTASerrializer(serializers.Serializer):
    email = serializers.CharField()
    name = serializers.CharField()
