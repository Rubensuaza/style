from django.urls import path

from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('/servicio_1',views.service_1,name='servicio1'),
    path('/who',views.whoAre,name='presentation')
   
]