from rest_framework import permissions

class IsManagerUser(permissions.BasePermission):
    """
    Custom permission to allow managers full access.
    """

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        return request.user.groups.filter(name='manager').exists()
