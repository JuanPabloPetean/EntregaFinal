from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('obras/', views.ObraListView.as_view(), name='lista_obras'),
    path('obras/<int:pk>/', views.ObraDetailView.as_view(), name='obra_detail'),
    path('obras/crear/', views.ObraCreateView.as_view(), name='crear_obra_cbv'),
    path('obras/<int:pk>/editar/', views.ObraUpdateView.as_view(), name='editar_obra'),
    path('obras/<int:pk>/eliminar/', views.ObraDeleteView.as_view(), name='eliminar_obra'),
]
