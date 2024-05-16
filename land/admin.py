from django.contrib import admin

from .models import Maintenance, Usage, Parcel, Paddock
# Register your models here.

admin.site.register(Usage)
admin.site.register(Maintenance)
admin.site.register(Parcel)
admin.site.register(Paddock)