from django.db import models
from .categorias import Categorias

class Preguntas(models.Model):
    id = models.AutoField(primary_key=True)
    pregunta = models.CharField(max_length=500)
    categ_id = models.ForeignKey(Categorias, related_name='level', on_delete=models.CASCADE)
   