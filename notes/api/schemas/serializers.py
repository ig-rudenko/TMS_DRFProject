from rest_framework import serializers


class SchemaImageUploadResponseSerializer(serializers.Serializer):
    image_url = serializers.URLField()
