from django.urls import path

from . import views

urlpatterns = [
    path('', views.login_router, name='login'),
    path('device/', views.save_device, name='device'),
    path('disconnect/<str:mac>/', views.disconnect_device, name='disconnect')
]

