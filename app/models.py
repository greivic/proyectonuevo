from django.db import models
from django.forms import model_to_dict


class Instrumento(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Nombre')
    color = models.CharField(max_length=150, verbose_name='Color')

    def __str__(self):
        return self.nombre

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Instrumento'
        verbose_name_plural = 'Instrumentos'
        db_table = 'instrumento'
        ordering = ['id']
