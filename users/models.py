from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.crypto import get_random_string

class User(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)

class Farm(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, related_name='owned_farms', on_delete=models.CASCADE)
    managers = models.ManyToManyField(User, related_name='managed_farms', blank=True)
    shareholders = models.ManyToManyField(User, related_name='shareholder_farms', blank=True)
    guests = models.ManyToManyField(User, related_name='guest_farms', blank=True)

    def __str__(self):
        return self.name

class Invitation(models.Model):
    INVITATION_ROLES = [
        ('MANAGER', 'Manager'),
        ('SHAREHOLDER', 'Shareholder'),
        ('GUEST', 'Guest'),
    ]

    email = models.EmailField()
    farm = models.ForeignKey(Farm, related_name='invitations', on_delete=models.CASCADE)
    role = models.CharField(max_length=15, choices=INVITATION_ROLES)
    token = models.CharField(max_length=50, default=get_random_string, unique=True)
    accepted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Invitation {self.email} to {self.farm.name} as {self.role}"
