from django.db import models

class Obra(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_estreno = models.DateField()
    genero = models.CharField(max_length=50)

    def __str__(self):
        return self.titulo
    