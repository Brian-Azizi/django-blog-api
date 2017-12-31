from blog_api.apps.core.renderers import BlogAPIJSONRenderer


class ProfileJSONRenderer(BlogAPIJSONRenderer):
    object_label = 'profile'
