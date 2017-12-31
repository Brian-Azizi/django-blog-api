import json

from rest_framework.renderers import JSONRenderer


class BlogAPIJSONRenderer(JSONRenderer):
    charset = 'utf-8'
    object_label = 'object'

    def render(self, data, media_type=None, renderer_context=None):
        # If the view throws an error, `data` will contain an `errors` key.
        # We want the default JSONRenderer to handle rendering errors.
        errors = data.get('errors', None)

        if errors is not None:
            return super(BlogAPIJSONRenderer, self).render(data)

        # Finally, we can render our data under the "user" namespace.
        return json.dumps({
            self.object_label: data
        })
