from django.contrib import admin

# Register your models here.
from .models import User, Farm, Invitation

admin.site.register(User)
admin.site.register(Farm)
admin.site.register(Invitation)