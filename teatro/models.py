from django.db import models

class Obra(models.Model):
    GENEROS = [
        ('Drama', 'Drama'),
        ('Comedia', 'Comedia'),
        ('Tragedia', 'Tragedia'),
        ('Musical', 'Musical'),
        ('Thriller', 'Thriller'),
        ('Experimental', 'Experimental'),
        ('Sainete', 'Sainete'),
        ('Otro', 'Otro'),
    ]
    
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_estreno = models.DateField()
    genero = models.CharField(max_length=50, choices=GENEROS, default='Otro')
    imagen = models.FileField(upload_to='obras/', null=True, blank=True)

    def __str__(self):
        return self.titulo
    
    class Meta:
        ordering = ['-fecha_estreno']
