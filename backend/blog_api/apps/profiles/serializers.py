from django.conf import settings
from rest_framework import serializers

from .models import Profile


class ImageSerializerField(serializers.URLField):
    def get_attribute(self, obj):
        # We pass the object instance onto `to_representation`,
        # not just the field attribute.
        return obj

    def to_representation(self, obj):
        if obj.image:
            return obj.image

        return settings.DEFAULT_IMAGE_URL

    def to_internal_value(self, data):
        return data


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    bio = serializers.CharField(allow_blank=True, required=False)
    image = ImageSerializerField(allow_blank=True)

    class Meta:
        model = Profile
        fields = ('username', 'bio', 'image',)
        read_only_fields = ('username',)
