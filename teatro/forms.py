from django import forms
from .models import Obra


class ObraForm(forms.ModelForm):
    class Meta:
        model = Obra
        fields = ['titulo', 'autor', 'descripcion', 'fecha_estreno', 'genero']
