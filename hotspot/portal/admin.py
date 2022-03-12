from django.contrib import admin

from .models import Device

# Register your models here.
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['id','mac','ip','account','last_login','logged_in','hotspot']

admin.site.register(Device,DeviceAdmin)