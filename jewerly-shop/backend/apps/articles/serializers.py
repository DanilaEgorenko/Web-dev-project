from rest_framework import serializers


class ArticleSerializer(serializers.Serializer):
    """
    All fields of Articles model that can be accessed from api
    """
    title = serializers.CharField(verbose_name="Название")
    description = serializers.TextField(verbose_name="Название")
    createDate = serializers.DateField.auto_now_add(verbose_name="Дата создания")
    changeDate = serializers.DateField.auto_now(verbose_name="Дата изменения")
