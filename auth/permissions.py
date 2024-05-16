from rest_framework import permissions

class IsFarmOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner

class IsFarmManager(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user in obj.managers.all()

class IsFarmShareholder(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user in obj.shareholders.all()

class IsFarmGuest(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user in obj.guests.all()
