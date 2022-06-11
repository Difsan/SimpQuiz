from django.db import models

class Categorias(models.Model):
    id = models.AutoField(primary_key=True)
    nivel = models.IntegerField()
    puntaje = models.IntegerField()
