from pyexpat.errors import messages
from django.contrib import messages as msg
from re import template
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.http import JsonResponse
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from .forms import RouterForm
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

        
class AgregarRouter(CreateView):
    model = Router
    form_class = RouterForm    
    template_name = 'gestionRouter/formulario_agregar_router.html'    

    def get_success_url(self):
        msg.success(self.request,'Router {} guardado con exito'.format(self.object.name))
        return reverse_lazy('gestionRouter:panel')


class EditarRouter(UpdateView):
    model = Router
    form_class = RouterForm
    template_name = 'gestionRouter/formulario_editar_router.html'

    def get_context_data(self, **kwargs):
        contexto = super(EditarRouter,self).get_context_data(**kwargs)
        return contexto
        
    def get_success_url(self):
        msg.success(self.request,'Router {} guardado con exito'.format(self.object.name))
        return reverse_lazy('gestionRouter:panel')

class EliminarRouter(DeleteView):
    model = Router
    template_name = 'gestionRouter/includes/formulario_modal_eliminar_router.html'

    def delete(self, request, *args, **kwargs):
        if request.is_ajax():
            print('is ajax')
            self.object = self.get_object()
            self.object.delete()
            mensaje = msg.success(request,'Router eliminado con éxito')
            response = JsonResponse({'mensaje':mensaje},safe=False)
            response.status_code = 201
            return response
            
        else:
            return redirect('gestionRouter:panel')


def agregar_portal(request):
    return None

def enable_router_ssl(request,pk):
    return None

def conectar_router(request,pk):
    return None
