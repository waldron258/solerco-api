from rest_framework import permissions

class IsProductAdminOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.role in ["admin", "product_admin"]
        return False