from tkinter import Widget
from django import forms

from .models import Router, Interface


class RouterForm(forms.ModelForm):

    class Meta:
        model = Router
        fields = ('name', 'host_ip', 'api_port','api_ssl_port', 'username','password')

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
