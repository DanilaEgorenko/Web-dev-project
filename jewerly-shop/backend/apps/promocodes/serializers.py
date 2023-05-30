from rest_framework import serializers

from apps.promocodes.models import Promocode


class PromocodeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    count_of_uses_user = serializers.IntegerField(default=None, verbose_name="Количество использований от одного пользователя")
    count_of_uses = serializers.IntegerField(default=None, verbose_name="Количество использований")
    name = serializers.CharField(default=None, verbose_name="Название промокода", max_length=12)
    deadline = serializers.DateField(default=None, verbose_name="Срок действия")

    class Meta:
        model = Promocode
        fields = [
          "id", 
          "users", 
          "count_of_uses_user", 
          "count_of_uses", 
          "name", 
          "deadline"
        ]


class GetPromocodeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    count_of_uses_user = serializers.IntegerField(default=None, verbose_name="Количество использований от одного пользователя")
    count_of_uses = serializers.IntegerField(default=None, verbose_name="Количество использований")
    name = serializers.CharField(default=None, verbose_name="Название промокода", max_length=12)
    deadline = serializers.DateField(default=None, verbose_name="Срок действия")

    class Meta:
        model = Promocode
        fields = [
          "id", 
          "users", 
          "count_of_uses_user", 
          "count_of_uses", 
          "name", 
          "deadline"
        ]
