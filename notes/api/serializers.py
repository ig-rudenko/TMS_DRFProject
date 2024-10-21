from rest_framework import serializers

from users.api.serializers import UserPublicSerializer
from ..models import Note, Comment, Tag


class NoteCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = ('id', 'title', 'content', "image", "owner", 'created_at', 'updated_at')
        read_only_fields = ('id', 'owner', 'created_at', 'updated_at')
        extra_kwargs = {
            "content": {"write_only": True},
        }


class NoteSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer()

    class Meta:
        model = Note
        fields = ('id', 'title', 'content', "image", "owner", 'created_at', 'updated_at')
        read_only_fields = ('id', 'owner', 'created_at', 'updated_at')


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'content', "owner", 'created_at', 'updated_at')
        read_only_fields = ('id', 'owner', 'created_at', 'updated_at')


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('name', "color")
