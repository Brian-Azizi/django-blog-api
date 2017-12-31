from blog_api.apps.core.renderers import BlogAPIJSONRenderer


class ArticleJSONRenderer(BlogAPIJSONRenderer):
    object_label = 'article'
