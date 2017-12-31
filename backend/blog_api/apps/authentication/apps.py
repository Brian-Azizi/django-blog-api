from django.apps import AppConfig


class AuthenticationAppConfig(AppConfig):
    name = 'blog_api.apps.authentication'
    label = 'authentication'
    verbose_name = 'Authentication'

    def ready(self):
        import blog_api.apps.authentication.signals
