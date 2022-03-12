from django.shortcuts import render
from django.views.generic import ListView

from .models import Router


class ListaRouterYHostpot(ListView):
    template_name = 'gestionRouter/gestion_panel.html'
    context_object_name = 'routers'
    model = Router

    def get_context_data(self, **kwargs):
        context = super(ListaRouterYHostpot,self).get_context_data(**kwargs)
        """
        try:
            router = Router.objects.filter()[0]
            c = ManagerApi(host_ip=router.host_ip, username=router.username, password=router.password, ssl=router.certificate,
                    api_port=router.api_port, api_ssl_port=router.api_ssl_port)
            c.connect()
            estado = c.router_status()
            c.disconnect()
            context['estado'] = estado
        except:

            context['estado'] = {}
        """
        #context['hotspots'] = hotspot = Hotspot.objects.order_by('name')
        return context


    def get_queryset(self):
        return Router.objects.order_by('name')
        
         
def agregar_router(request):
    return None

def agregar_portal(request):
    return None

def enable_router_ssl(request,pk):
    return None

def conectar_router(request,pk):
    return None

def editar_router(request,pk):
    return None

def eliminar_router(request,pk):
    return None