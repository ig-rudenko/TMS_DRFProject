from rest_framework import serializers

from users.models import User


# class CommonCreateUserSerializer(serializers.Serializer):
#     username = serializers.CharField(max_length=150)
#     email = serializers.EmailField()
#     password = serializers.CharField(max_length=100)
#
#
# class CommonUserSerializer(serializers.Serializer):
#     username = serializers.CharField(max_length=150)
#     email = serializers.EmailField()
#     first_name = serializers.CharField(max_length=150)
#     last_name = serializers.CharField(max_length=150)
#     is_active = serializers.BooleanField()
#     is_staff = serializers.BooleanField()
#     is_superuser = serializers.BooleanField()
#     last_login = serializers.DateTimeField()
#     date_joined = serializers.DateTimeField()
#     phone = serializers.CharField(max_length=15)
#     address = serializers.CharField(max_length=100)


class UserPublicSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "date_joined",
        )

        read_only_fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "date_joined",
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
            "is_active",
            "is_staff",
            "is_superuser",
            "last_login",
            "date_joined",
            "phone",
            "address",
        )
        read_only_fields = (
            "id",
            "first_name",
            "last_name",
            "is_active",
            "is_staff",
            "is_superuser",
            "last_login",
            "date_joined",
            "phone",
            "address",
        )
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data) -> User:
        user = User.objects.create_user(
            validated_data["username"], validated_data["email"], validated_data["password"]
        )
        return user
