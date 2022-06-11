from django.db import models
from .preguntas import Preguntas
from .participante import Participante

class Participacion(models.Model):
    id = models.AutoField(primary_key=True)
    ronda = models.CharField(max_length=20)
    preguntaId = models.ForeignKey(Preguntas, related_name='pregunId', on_delete=models.CASCADE)
    participanteId = models.ForeignKey(Participante, related_name='partiId', on_delete=models.CASCADE)
    puntaje_Ronda = models.IntegerField(default=0)
    