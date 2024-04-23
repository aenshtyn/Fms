from django.contrib import admin

# Register your models here.
from .models import Production, Feeds

admin.site.register(Production)
admin.site.register(Feeds)