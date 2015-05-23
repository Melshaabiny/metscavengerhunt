from django.contrib import admin
# Register your models here.
from cr_hunt.models import cr_Hunts, cr_Has

admin.site.register(cr_Hunts)
admin.site.register(cr_Has)