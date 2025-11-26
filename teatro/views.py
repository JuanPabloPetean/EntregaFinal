from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Obra
from .forms import ObraForm


def home(request):
    return render(request, 'teatro/home.html')


def about(request):
    return render(request, 'teatro/about.html')


class ObraListView(ListView):
    model = Obra
    template_name = 'teatro/lista_obras.html'
    context_object_name = 'obras'
    paginate_by = 10


def lista_obras(request):
    obras = Obra.objects.all()
    return render(request, 'teatro/lista_obras.html', {'obras': obras})


class ObraDetailView(DetailView):
    model = Obra
    template_name = 'teatro/obra_detail.html'
    context_object_name = 'obra'


class ObraCreateView(LoginRequiredMixin, CreateView):
    model = Obra
    form_class = ObraForm
    template_name = 'teatro/crear_obra.html'
    success_url = reverse_lazy('lista_obras')
    
    def form_valid(self, form):
        messages.success(self.request, 'Obra creada exitosamente.')
        return super().form_valid(form)


def crear_obra(request):
    if request.method == 'POST':
        form = ObraForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Obra creada exitosamente.')
            return redirect('lista_obras')
    else:
        form = ObraForm()
    return render(request, 'teatro/crear_obra.html', {'form': form})


class ObraUpdateView(LoginRequiredMixin, UpdateView):
    model = Obra
    form_class = ObraForm
    template_name = 'teatro/editar_obra.html'
    success_url = reverse_lazy('lista_obras')
    
    def form_valid(self, form):
        messages.success(self.request, 'Obra actualizada exitosamente.')
        return super().form_valid(form)


class ObraDeleteView(LoginRequiredMixin, DeleteView):
    model = Obra
    template_name = 'teatro/eliminar_obra.html'
    success_url = reverse_lazy('lista_obras')
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Obra eliminada exitosamente.')
        return super().delete(request, *args, **kwargs)
