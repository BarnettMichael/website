from rest_framework import permissions


class IsUserAllowedToWrite(permissions.BasePermission):
    """
    Custom permission to only allow changes to database if user is Mike or Toni
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True


        return request.user in ['Mike', 'mike', 'Toni']