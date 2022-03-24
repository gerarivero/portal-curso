from tkinter import Widget

from django import forms
from django.core.exceptions import ValidationError

from .models import Router, Interface


class RouterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(render_value = True))
    class Meta:
        model = Router
        fields = ('name', 'host_ip', 'dns','api_port','api_ssl_port', 'username','password')


    def __init__(self, *args, **kwargs):
        super(RouterForm,self).__init__(*args, **kwargs)
        
        self.fields['dns'].required = False
        self.fields['host_ip'].required = False

        #instance = kwargs.pop('instance', '')
        #if instance:
        #   self.fields['host_ip'].widget.attrs['readonly'] = True
           


    def clean(self):
        """
        clean es para validar fields que dependen de otros fields 
            * Al usar add_error(field,error) el error se pinta en el imput correpondiente al field
            * con raise ValidationError('error') el mensaje se carga en la coleccion del formulario llamada {{ form.non_field_errors }} 
              que se debera recorre y mostrar los mensajes en el template del formulario
        """
        cleaned_data = super().clean()
        dns = cleaned_data['dns']
        host_ip = cleaned_data['host_ip']
        
        if dns != None and host_ip:
            self.add_error('dns',ValidationError('Debe ingresar un valor en Host ip o Dns, no en los dos a la vez'))
            self.add_error('host_ip',ValidationError('Debe ingresar un valor en Host ip o Dns, no en los dos a la vez'))
        
        if dns == None and not host_ip:
            self.add_error('dns',ValidationError('Debe ingresar un valor en Host ip o Dns, no en los dos a la vez'))
            self.add_error('host_ip',ValidationError('Debe ingresar un valor en Host ip o Dns, no en los dos a la vez'))