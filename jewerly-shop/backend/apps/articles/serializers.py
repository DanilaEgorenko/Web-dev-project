from rest_framework import serializers

from apps.articles.models import Article


class ArticleSerializer(serializers.Serializer):
    class Meta:
        model = Article
        fields = ["id", "title", "description", "create_date", "change_date"]