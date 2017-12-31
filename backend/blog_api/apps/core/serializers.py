from rest_framework import serializers


class TimestampedModelSerializer(serializers.ModelSerializer):
    # The client expects `created_at` to be called `createdAt`
    # and `updated_at` to be `updatedAt`.
    createdAt = serializers.SerializerMethodField(method_name='get_created_at')
    updatedAt = serializers.SerializerMethodField(method_name='get_updated_at')

    def get_created_at(self, instance):
        return instance.created_at.isoformat()

    def get_updated_at(self, instance):
        return instance.updated_at.isoformat()
