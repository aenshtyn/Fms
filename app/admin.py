from django.contrib import admin

# Register your models here.
from app.models import Employee, Inventory, Crop, Livestock, Feed, FeedConsumption 


admin.site.register(Employee)
admin.site.register(Inventory)
admin.site.register(Crop)
admin.site.register(Livestock)
admin.site.register(Feed)
admin.site.register(FeedConsumption)