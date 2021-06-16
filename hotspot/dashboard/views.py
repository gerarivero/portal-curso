from django.shortcuts import render
from django.views.generic import ListView
from portal.models import Device

class dashboard(ListView):
    model = Device
    template_name = 'dashboard/conectados.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        contexto = super(dashboard, self).get_context_data(**kwargs)
        dispositivos = Device.objects.filter(logged_in=True)
        contexto['dispositivos'] = dispositivos
        print(contexto)
        return contexto
        




