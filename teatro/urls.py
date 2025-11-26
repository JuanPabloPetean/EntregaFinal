from django.urls import path
from . import views

urlpatterns = [
    path('obras/', views.lista_obras, name='lista_obras'),
    path('obras/nueva/', views.crear_obra, name='crear_obra'),
]
