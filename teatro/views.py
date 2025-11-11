from django.shortcuts import render
from .models import Obra

def lista_obras(request):
    obras = Obra.objects.all()
    return render(request, 'teatro/lista_obras.html', {'obras': obras})

