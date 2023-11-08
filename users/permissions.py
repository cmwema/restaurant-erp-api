from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsManagerUser(permissions.BasePermission):
    """
    Custom permission to allow managers full access.
    """

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        return request.user.groups.filter(name="manager").exists()


class IsAnonymousUser(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return True
        return False
