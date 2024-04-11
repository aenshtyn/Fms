from django.contrib import admin

from .models import Maintenance, Usage, Parcel
# Register your models here.

admin.site.register(Usage)
admin.site.register(Maintenance)
admin.site.register(Parcel)