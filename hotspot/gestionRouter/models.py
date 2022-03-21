from operator import mod
from django.db import models

# Create your models here.
class Router(models.Model):
    name = models.CharField(max_length=30)
    host_ip = models.GenericIPAddressField(null=True)
    dns = models.CharField(max_length=40,null=True)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    api_port = models.IntegerField(default=8728)
    api_ssl_port = models.IntegerField(default=8729)
    certificate = models.BooleanField(default=False)
    connected = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

"""
class Router_Planes(models.Model):
    router = models.ForeignKey(Router,on_delete=models.CASCADE,related_name='planes')
    plan = models.ForeignKey(PlanNavegacion,related_name='routers')
"""
class Interface(models.Model):
    router = models.ForeignKey(Router, on_delete=models.CASCADE)
    default_name = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    comment = models.CharField(max_length=50, null=True)
    ip_address = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('router', 'default_name')
"""
class Hotspot(models.Model):
    router = models.ForeignKey(Router, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    domain = models.URLField(max_length=100)
    enable = models.BooleanField(default=False)
    login_template = models.ForeignKey(PlantillaLogin, null=True)
    advertise_page = models.CharField(max_length=50, null=True)
    installed = models.BooleanField(default=False)
    plan_social = models.ForeignKey(PlanNavegacion,null=True)
    network_address = models.CharField(default='10.100.22.0/24', max_length=50)
    pool_name= models.CharField(default='pool', max_length=30)
    interface = models.ForeignKey(Interface, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
"""