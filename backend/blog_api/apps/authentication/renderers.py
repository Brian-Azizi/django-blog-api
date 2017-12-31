import json

from blog_api.apps.core.renderers import BlogAPIJSONRenderer


class UserJSONRenderer(BlogAPIJSONRenderer):
    object_label = 'user'

    def render(self, data, media_type=None, renderer_context=None):
        # If we receive a `token` key as part of the response, it will be a
        # byte object. Byte objects don't serialize well, so we need to
        # decode it before rendering the User object.
        token = data.get('token', None)

        if token is not None and isinstance(token, bytes):
            data['token'] = token.decode('utf-8')

        # Finally, we can render our data under the "user" namespace.
        return super(UserJSONRenderer, self).render(data)
