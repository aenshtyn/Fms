from rest_framework import permissions
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from .models import CustomUser

content_type = ContentType.objects.get_for_model(CustomUser)
Permission.objects.create(
    codename='view_farm_dashboard',
    name='Can view farm dashboard',
    content_type=content_type,
)



# class IsFarmOwner(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         return request.user == obj.owner

# class IsFarmManager(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         return request.user in obj.managers.all()

# class IsFarmShareholder(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         return request.user in obj.shareholders.all()

# class IsFarmGuest(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         return request.user in obj.guests.all()
