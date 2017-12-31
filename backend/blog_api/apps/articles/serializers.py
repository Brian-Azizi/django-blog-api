from rest_framework import serializers

from blog_api.apps.core.serializers import TimestampedModelSerializer
from blog_api.apps.profiles.serializers import ProfileSerializer

from .models import Article, Comment


class ArticleSerializer(TimestampedModelSerializer):
    author = ProfileSerializer(read_only=True)
    description = serializers.CharField(required=False)
    slug = serializers.SlugField(required=False)

    class Meta:
        model = Article
        fields = (
            'author',
            'body',
            'createdAt',
            'description',
            'slug',
            'title',
            'updatedAt',
        )

    def create(self, validated_data):
        author = self.context.get('author', None)

        return Article.objects.create(author=author, **validated_data)


class CommentSerializer(TimestampedModelSerializer):
    author = ProfileSerializer(required=False)

    class Meta:
        model = Comment
        fields = (
            'id',
            'author',
            'body',
            'createdAt',
            'updatedAt',
        )

    def create(self, validated_data):
        article = self.context['article']
        author = self.context['author']

        return Comment.objects.create(
            author=author, article=article, **validated_data
        )
