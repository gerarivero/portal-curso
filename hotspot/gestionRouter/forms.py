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
        
        self.fields['dns'].required = False
        self.fields['host_ip'].required = False

        instance = kwargs.pop('instance', '')
        if instance:
           self.fields['host_ip'].widget.attrs['readonly'] = True
           


    def clean(self):
        cleaned_data = super().clean()
        dns = cleaned_data['dns']
        host_ip = cleaned_data['host_ip']

        
        if dns != None and host_ip != None:
            self.add_error('dns',ValidationError('Debe ingresar un valor en host ip o dns'))
            self.add_error('host_ip',ValidationError('Debe ingresar un valor en host ip o dns'))
        
        if dns == None and host_ip == None:
            self.add_error('dns',ValidationError('Debe ingresar un valor en host ip o dns'))
            self.add_error('host_ip',ValidationError('Debe ingresar un valor en host ip o dns'))