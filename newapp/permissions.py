from rest_framework import permissions 
from .models import User, Books


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)

class IsAdminAndManagerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user.role == User.SUPER_USER or request.user.role == User.MANAGER)

class IsAdminAndAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user.role == User.SUPER_USER or request.user.role == User.MANAGER or request.user == Books.author)