from django.test import TestCase

from users.api.serializers import UserSerializer
from ..models import User


class TestUserSerializer(TestCase):

    def test_user_serializer_password_encryption(self):
        data = {"username": "test", "password": "test", "email": "test@test.com"}

        serializer = UserSerializer(data=data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        user = User.objects.get(username="test")
        print(user.password)
        self.assertIn("pbkdf2_sha256", user.password)
        self.assertNotEqual(user.password, data["password"])
