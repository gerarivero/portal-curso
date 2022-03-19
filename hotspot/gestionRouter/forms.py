from tkinter import Widget
from django import forms
from django.core.exceptions import ValidationError

from .models import Router, Interface


class RouterForm(forms.ModelForm):

    class Meta:
        model = Router
        fields = ('name', 'host_ip', 'dns','api_port','api_ssl_port', 'username','password')



        widget = {
            'password' : forms.PasswordInput(
                render_value=True
            )
        }

    def __init__(self, *args, **kwargs):
        super(RouterForm,self).__init__(*args, **kwargs)
        instance = kwargs.pop('instance', '')
        if instance:
           self.fields['host_ip'].widget.attrs['readonly'] = True


    def clean_dns(self):
        dns = self.cleaned_data['dns']
        host_ip = self.cleaned_data['host_ip']

        if len(dns) > 0 and len(host_ip) > 0:
            raise ValidationError('Debe ingresar un valor en host_ip o dns')
        
        if len(dns) == 0 and len(host_ip) == 0:
            raise ValidationError('Debe ingresar un valor en host_ip o dns')

        return dns