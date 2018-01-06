import json

from rest_framework.renderers import JSONRenderer
from rest_framework.utils.serializer_helpers import ReturnList


class BlogAPIJSONRenderer(JSONRenderer):
    charset = 'utf-8'
    object_label = 'object'
    pagination_object_label = 'objects'
    pagination_count_label = 'count'

    def render(self, data, media_type=None, renderer_context=None):
        if data.get('results', None) is not None:
            return json.dumps({
                self.pagination_object_label: data['results'],
                self.pagination_count_label: data['count']
            })

        elif data.get('errors', None) is not None:
            # If the view throws an error, `data` will contain an `errors` key.
            # We want the default JSONRenderer to handle rendering errors.
            return super(BlogAPIJSONRenderer, self).render(data)

        else:
            return json.dumps({
                self.object_label: data
            })
