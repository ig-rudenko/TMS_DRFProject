from django.test import TestCase, Client
from django.shortcuts import reverse
from rest_framework.test import APIClient
from django.conf import settings

from ..models import User


class TestExample(TestCase):

    @classmethod
    def setUpTestData(cls):
        """Запускается один раз"""
        print("setUpTestData")
        User.objects.create_user("test", "test@test.com", "test")
        User.objects.create_user("test2", "test2@test.com", "test")

    def setUp(self):
        """Запускается перед каждым тестом (методом)"""
        print("setUp")

    def tearDown(self):
        """Запускается после каждого теста (метода)"""
        print("tearDown")

    def test_user_can_create_a_post(self):
        """
        Test if a user can create a post
        """
        User.objects.all().delete()
        print("1", User.objects.all())

    def test_user_can_update_a_post(self):
        """
        Test if a user can update a post
        """
        print("2", User.objects.all())

    def test_user_can_delete_a_post(self):
        """
        Test if a user can delete a post
        """
        print("3", User.objects.all())

    def test_user_can_view_a_post(self):
        """
        Test if a user can view a post
        """
        print("4", User.objects.all())


class TestCreateUserPermissions(TestCase):
    """
    Тестируем права на создание пользователя
    """

    @classmethod
    def setUpTestData(cls):
        cls.client = APIClient()
        # /api/v1/users/
        cls.url = reverse("users-api-v1:list-create")

    def test_create_user_by_anonymous(self):
        response = self.client.post(
            self.url,
            {
                "username": "test",
                "email": "test@test.com",
                "password": "test",
            },
            format="json",
        )
        self.assertEqual(response.status_code, 201)

    def test_create_user_without_email_by_anonymous(self):
        response = self.client.post(
            self.url,
            {
                "username": "test",
                "password": "test",
            },
            format="json",
        )
        self.assertEqual(response.status_code, 400)

    def test_create_user_with_empty_username_by_anonymous(self):
        response = self.client.post(
            self.url,
            {
                "username": "",
                "email": "test@test.com",
                "password": "test",
            },
            format="json",
        )
        self.assertEqual(response.status_code, 400)

    def test_cant_read_user_list_by_anonymous(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 403)

    def test_can_read_user_list_by_superuser(self):
        User.objects.create_superuser("test", "test@test.com", "test")
        superuser = User.objects.create_superuser("superuser", "superuser@test.com", "superuser")
        self.client.force_login(superuser)

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200, "Ошибка при получении списка пользователей")

        self.assertIn("count", response.data, "Не возвращается кол-во пользователей в ответе")

        self.assertEqual(response.data["count"], 2)
        self.assertEqual(len(response.data["results"]), 2)
