from django.contrib import admin

# Register your models here.
from .models import MilkProduction, DairyFeeds

admin.site.register(MilkProduction)
admin.site.register(DairyFeeds)