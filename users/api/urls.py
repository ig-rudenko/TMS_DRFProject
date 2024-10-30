from django.urls import path

from . import views


app_name = "users-api-v1"

urlpatterns = [
    path("", views.UserListCreateAPIView.as_view(), name="list-create"),
    path("myself", views.UserDetailAPIView.as_view(), name="myself"),
]
