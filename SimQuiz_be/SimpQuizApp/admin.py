# Register your models here.
from django.contrib import admin
from .models.categorias import Categorias
from .models.participacion import Participacion
from .models.participante import Participante
from .models.preguntas import Preguntas
from .models.respuestas import Respuestas

admin.site.register(Categorias)
admin.site.register(Participacion)
admin.site.register(Participante)
admin.site.register(Preguntas)
admin.site.register(Respuestas)