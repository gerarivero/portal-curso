from django.contrib import admin

# Register your models here.
from .models import Router, Interface

# Register your models here.
class RouterAdmin(admin.ModelAdmin):
    list_display = ['id','name','host_ip','username','password','api_port','api_ssl_port','certificate','connected','timestamp']

admin.site.register(Router,RouterAdmin)

class InterfaceAdmin(admin.ModelAdmin):
    list_display = ['id','router','default_name','name','comment','ip_address',]

admin.site.register(Interface,InterfaceAdmin)