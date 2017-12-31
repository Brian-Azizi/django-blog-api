from django.apps import AppConfig


class ArticlesAppConfig(AppConfig):
    name = 'blog_api.apps.articles'
    label = 'articles'
    verbose_name = 'Articles'

    def ready(self):
        import blog_api.apps.articles.signals
