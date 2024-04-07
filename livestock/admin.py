from django.contrib import admin
from .models import Animal, Health, Breeding, Reproduction, Vaccination, Mortality


admin.site.register(Animal)
admin.site.register(Health)
admin.site.register(Breeding)
admin.site.register(Reproduction)
admin.site.register(Vaccination)
admin.site.register(Mortality)