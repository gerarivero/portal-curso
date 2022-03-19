from pyexpat.errors import messages
from django.contrib import messages as msg
from re import template
from django.views.generic import ListView,CreateView,UpdateView

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
"""
class AgregarRouterJson(CreateView):
    template_name = 'gestionRouter/includes/formulario_modal_agregar_router.html'
    model = Router
    form_class = RouterForm

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            print('is ajax')
            formulario = self.form_class(request.POST)
            if formulario.is_valid():
                formulario.save()
                #mensaje = msg.success(request,'Router registrado con éxito')
                #response = JsonResponse({'messages':mensaje})
                # obtener la lista de router para mostrar en la tabla
                html['html_table-router_tbody'] = render_to_string()
                response = JsonResponse(html)
                response.status_code = 200
                return response
            else:
                print('fomulario INVALIDO')
                html = dict()
                html['html_formulario'] = render_to_string(self.template_name,{'form':formulario},request)
                response = JsonResponse(html)
                response.status_code = 400
                return response
        else:
            print('no es ajax')
            return redirect('gestionRouter:panel')
"""

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