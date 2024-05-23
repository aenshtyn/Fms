from django.contrib import admin

# Register your models here.
from .models import CustomUser, Farm, UserFarmRole

admin.site.register(CustomUser)
admin.site.register(Farm)
admin.site.register(UserFarmRole)