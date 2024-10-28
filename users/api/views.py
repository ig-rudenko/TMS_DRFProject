from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework import status
from django.core.cache import cache

from .permissions import PostAnyOrSuperuserPermission
from .serializers import UserSerializer
from ..models import User


# Function based view


@api_view(["POST", "GET"])
@permission_classes([IsAdminUser])
def create_user_fbv_api(request):
    if request.method == "POST":
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    else:
        # Method POST
        serializer = UserSerializer(User.objects.all(), many=True)
        return Response(serializer.data)


class UserListCreateAPIView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [PostAnyOrSuperuserPermission]

    def get(self, request, *args, **kwargs):
        page = self.request.query_params.get("page", 1)
        cache_key = f"user_lists:{page}"
        cache_timeout = 10 * 60

        data = cache.get(cache_key)
        if data is None:
            print("cache miss")
            response = super().get(request, *args, **kwargs)
            data = response.data
            cache.set(cache_key, data, cache_timeout)

        return Response(data)
