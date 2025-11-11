from django.urls import path
from . import views

urlpatterns = [
    path('obras/', views.lista_obras, name='lista_obras'),
]
