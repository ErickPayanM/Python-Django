from django.db import models

# Create your models here.

class Articulos(models.Model):
    Articulo = models.CharField(max_length=150)
    Description = models.TextField()
    Cantidad = models.IntegerField(default=0)
    def __str__(self):
        return self.Articulo