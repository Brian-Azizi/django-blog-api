from blog_api.apps.core.renderers import BlogAPIJSONRenderer


class ProfileJSONRenderer(BlogAPIJSONRenderer):
    object_label = 'profile'
    pagination_object_label = 'profiles'
    pagination_count_label = 'profilesCount'
