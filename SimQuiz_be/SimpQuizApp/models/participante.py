from django.db import models


class Participante(models.Model):
    id = models.BigAutoField(primary_key=True)
    nickname = models.CharField( max_length = 25, unique=True)
    puntaje_Total = models.IntegerField(default=0)

