from django.contrib import admin

# Register your models here.
from app.models import Employee, Inventory, Crop, Feed


admin.site.register(Employee)
admin.site.register(Inventory)
admin.site.register(Crop)
admin.site.register(Feed)
