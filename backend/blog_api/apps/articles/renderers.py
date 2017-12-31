from blog_api.apps.core.renderers import BlogAPIJSONRenderer


class ArticleJSONRenderer(BlogAPIJSONRenderer):
    object_label = 'article'
    object_label_plural = 'articles'


class CommentJSONRenderer(BlogAPIJSONRenderer):
    object_label = 'comment'
    object_label_plural = 'comments'
