from rest_framework import permissions
from iot.models import Device

class IsOwnerDevice(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user
