from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard.as_view(), name='dashboard'),

]