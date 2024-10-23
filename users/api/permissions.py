from rest_framework.permissions import BasePermission, SAFE_METHODS


class PostAnyOrSuperuserPermission(BasePermission):
    def has_permission(self, request, view) -> bool:
        return request.method == "POST" or request.user.is_superuser
