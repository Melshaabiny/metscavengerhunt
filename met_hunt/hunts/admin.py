from django.contrib import admin
from hunts.models import Hunts, Items, Has

# Register your models here.
admin.site.register(Hunts)
admin.site.register(Items)
admin.site.register(Has)