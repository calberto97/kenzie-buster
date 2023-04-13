from rest_framework import permissions
from rest_framework.request import Request
from .models import User


class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request: Request, view, obj: User):
        if obj == request.user:
            return True
        elif request.user.is_authenticated and request.user.is_employee:
            return True
