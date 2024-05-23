from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.crypto import get_random_string

class Farm(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='owned_farms')

    def __str__(self):
        return self.name
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('owner', 'Farm Owner'),
        ('manager', 'Manager'),
        ('shareholder', 'Shareholder'),
        ('guest', 'Guest'),
    )
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default= 'Farm Owner')
    farms = models.ManyToManyField(Farm, through='UserFarmRole')
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # Specify related_name to avoid conflict
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',  # Specify related_name to avoid conflict
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='user',
    )



class UserFarmRole(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    role = models.CharField(max_length=15, choices=CustomUser.ROLE_CHOICES)


