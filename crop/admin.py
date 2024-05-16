from django.contrib import admin

# Register your models here.
from .models import Crop, CropCycle, CropHealth, PestControl, Harvest

admin.site.register(Crop)
admin.site.register(CropCycle)
admin.site.register(CropHealth)
admin.site.register(PestControl)
admin.site.register(Harvest)