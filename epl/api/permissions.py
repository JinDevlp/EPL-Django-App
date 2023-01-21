from rest_framework.permissions import BasePermission, SAFE_METHODS

# Allow Admin to POST and Non-Admin to GET
class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return request.user.is_staff