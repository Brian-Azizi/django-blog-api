from rest_framework import serializers

from blog_api.apps.core.serializers import TimestampedModelSerializer
from blog_api.apps.profiles.serializers import ProfileSerializer

from .models import Article, Comment


class ArticleSerializer(TimestampedModelSerializer):
    author = ProfileSerializer(read_only=True)
    description = serializers.CharField(required=False)
    slug = serializers.SlugField(required=False)

    favorited = serializers.SerializerMethodField()
    favorites_count = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = (
            'author',
            'body',
            'createdAt',
            'description',
            'favorited',
            'favorites_count',
            'slug',
            'title',
            'updatedAt',
        )

    def create(self, validated_data):
        author = self.context.get('author', None)

        return Article.objects.create(author=author, **validated_data)

    def get_favorited(self, instance):
        request = self.context.get('request', None)

        if request is None:
            return False

        if not request.user.is_authenticated:
            return False

        return request.user.profile.has_favorited(instance)

    def get_favorites_count(self, instance):
        return instance.favorited_by.count()

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


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('tag',)

    def to_representation(self, obj):
        return obj.tag
