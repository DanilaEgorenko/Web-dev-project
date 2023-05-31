from rest_framework import serializers
from .models import Good


class GoodSerializer(serializers.Serializer):
    """
    All fields of Goods model that can be accessed from api
    """
    title = serializers.CharField(max_length=64)
    price = serializers.DecimalField(max_digits=9, decimal_places=2)
    category = None
    material = serializers.CharField(max_length=64)
    src = serializers.SerializerMethodField('get_image_url')
    color = serializers.CharField(max_length=32)
    
    class Meta:
        model = Good
        fields = ('title', 'price', 'src', 'category', 'material', 'color')

    def get_image_url(self, obj):
        result = obj.img.url[7:]
        return result
