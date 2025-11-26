from django.shortcuts import render, redirect
from .models import Obra
from .forms import ObraForm


def lista_obras(request):
    obras = Obra.objects.all()
    return render(request, 'teatro/lista_obras.html', {'obras': obras})


def crear_obra(request):
    if request.method == 'POST':
        form = ObraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_obras')
    else:
        form = ObraForm()
    return render(request, 'teatro/crear_obra.html', {'form': form})

