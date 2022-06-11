from django.db import models
from .preguntas import Preguntas

class Respuestas(models.Model):
    id = models.AutoField(primary_key=True)
    respuesta = models.CharField('Respuesta', max_length=150)
    preg_Id = models.ForeignKey(Preguntas, related_name='pre', on_delete=models.CASCADE)
    correcta = models.BooleanField(default=False)

