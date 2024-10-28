from rest_framework import serializers

from users.api.serializers import UserPublicSerializer
from ..models import Note, Comment, Tag


class ImageUploadSerializer(serializers.Serializer):
    image = serializers.ImageField()


class TagSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)

    class Meta:
        model = Tag
        fields = ("name", "color")
        # extra_kwargs = {
        #     "name": {"validators": []},  # Отключаем проверку уникальности
        # }


class NoteCreateSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Note
        fields = (
            "id",
            "title",
            "content",
            "image",
            "owner",
            "created_at",
            "updated_at",
            "tags",
        )
        read_only_fields = ("id", "owner", "created_at", "updated_at")
        extra_kwargs = {
            "content": {"write_only": True},
        }

    def validate_title(self, value: str) -> str:
        if len(value) < 3:
            raise serializers.ValidationError("Title must be at least 3 characters")
        if value[0].isdigit():
            raise serializers.ValidationError("Title must start with a letter")
        return value

    def validate(self, data):
        if data["title"] == data["content"]:
            raise serializers.ValidationError("Title and content must be different")
        return data

    def create(self, validated_data):
        # Вытягиваем данные тега по ключу и удалить его.
        tags_data: list[dict] = validated_data.pop("tags")

        model_tags = []
        for tag_data in tags_data:
            # tag_data = {
            #     "name": "python",
            #     "color": "#121212"
            # }

            # try:
            #     tag = Tag.objects.get(name=tag_data["name"])
            # except Tag.DoesNotExist:
            #     tag = Tag.objects.create(**tag_data)
            # model_tags.append(tag)

            # Идентично
            # Возвращает кортеж, содержащий тег и статус создания.
            # Распаковываем с помощью `tag, _ = `
            tag, _ = Tag.objects.get_or_create(
                name=tag_data["name"],
                defaults={
                    "color": tag_data.get("color", "#000000")
                },  # Задаем цвет по умолчанию
            )
            model_tags.append(tag)

        note = Note.objects.create(**validated_data)
        note.tags.set(model_tags)
        return note


class NoteShortSerializer(serializers.ModelSerializer):
    short_content = serializers.SerializerMethodField()
    tags = TagSerializer(many=True)
    owner = serializers.CharField(source="owner.username")
    image = serializers.CharField()

    class Meta:
        model = Note
        fields = (
            "id",
            "title",
            "content",
            "short_content",
            "image",
            "owner",
            "created_at",
            "updated_at",
            "tags",
        )
        read_only_fields = ("id", "owner", "created_at", "updated_at")
        extra_kwargs = {
            "content": {"write_only": True},
        }

    def get_short_content(self, obj):
        return getattr(obj, "short_content", None)


class NoteSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer()
    tags = TagSerializer(many=True)

    class Meta:
        model = Note
        fields = (
            "id",
            "title",
            "content",
            "image",
            "owner",
            "created_at",
            "updated_at",
            "tags",
        )
        read_only_fields = ("id", "owner", "created_at", "updated_at")

    def update(self, instance, validated_data):
        # Вытягиваем данные тега по ключу и удалить его.
        tags_data = validated_data.pop("tags")

        note = super().update(instance, validated_data)

        model_tags = []
        for tag_data in tags_data:
            # tag_data = {
            #     "name": "python",
            #     "color": "#121212"
            # }

            # try:
            #     tag = Tag.objects.get(name=tag_data["name"])
            # except Tag.DoesNotExist:
            #     tag = Tag.objects.create(**tag_data)
            # model_tags.append(tag)

            # Идентично
            # Возвращает кортеж, содержащий тег и статус создания.
            # Распаковываем с помощью `tag, _ = `
            tag, _ = Tag.objects.get_or_create(
                name=tag_data["name"],
                defaults={
                    "color": tag_data.get("color", "#000000")
                },  # Задаем цвет по умолчанию
            )
            model_tags.append(tag)

        note.tags.set(model_tags)
        return note


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ("id", "content", "owner", "created_at", "updated_at")
        read_only_fields = ("id", "owner", "created_at", "updated_at")
