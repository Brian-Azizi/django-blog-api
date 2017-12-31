from rest_framework import generics, mixins, status, viewsets
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Article, Comment
from .renderers import ArticleJSONRenderer, CommentJSONRenderer
from .serializers import ArticleSerializer, CommentSerializer


class ArticleViewSet(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    lookup_field = 'slug'
    queryset = Article.objects.select_related('author', 'author__user')
    permission_classes = (IsAuthenticatedOrReadOnly,)
    renderer_classes = (ArticleJSONRenderer,)
    serializer_class = ArticleSerializer

    def create(self, request):
        serializer_context = {'author': request.user.profile}
        serializer_data = request.data.get('article', {})

        serializer = self.serializer_class(
            data=serializer_data, context=serializer_context
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, slug):
        try:
            serializer_instance = self.queryset.get(slug=slug)
        except Article.DoesNotExist:
            raise NotFound('An article with this slug does not exist.')

        serializer = self.serializer_class(serializer_instance)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, slug):
        try:
            serializer_instance = self.queryset.get(slug=slug)
        except Article.DoesNotExist:
            raise NotFound('An article with this slug does not exist.')

        serializer_data = request.data.get('article', {})
        serializer = self.serializer_class(
            serializer_instance, data=serializer_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


class CommentsListCreateAPIView(generics.ListCreateAPIView):
    lookup_field = 'article__slug'
    lookup_url_kwarg = 'article_slug'
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Comment.objects.select_related(
        'article', 'article__author', 'article__author__user',
        'author', 'author__user'
    )
    renderer_classes = (CommentJSONRenderer,)
    serializer_class = CommentSerializer

    def filter_queryset(self, queryset):
        # The built-in list function calls `filter_queryset`. Since we
        # only want comments for a specific article, this is a good place
        # to do that filtering.
        filters = {self.lookup_field: self.kwargs[self.lookup_url_kwarg]}

        return queryset.filter(**filters)
