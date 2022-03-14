from django.conf.urls import url

from . import views

app_name = 'gestionRouter'

urlrouter = [

    url(r'^$', views.ListaRouterYHostpot.as_view(), name='panel'),
    #url(r'^agregar_router', views.agregar_router, name='agregar_router'),
    url(r'^agregar_router', views.AgregarRouter.as_view(), name='agregar_router'),
    
    url(r'^eliminar_router/(?P<pk>\d+)', views.eliminar_router, name='eliminar_router'),
    url(r'^editar_router/(?P<pk>\d+)', views.editar_router, name='editar_router'),
    url(r'^enable_router_ssl/(?P<pk>\d+)', views.enable_router_ssl, name='enable_router_ssl'),
    url(r'^conectar_router/(?P<pk>\d+)', views.conectar_router, name='conectar_router'),
    
]

urlhostpot = [
    url(r'^agregar_portal', views.agregar_portal, name='agregar_portal'),
]

urlpatterns = urlrouter + urlhostpot
