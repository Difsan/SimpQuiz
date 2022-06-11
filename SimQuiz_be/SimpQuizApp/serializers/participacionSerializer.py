from SimpQuizApp.models.participacion import Participacion
from SimpQuizApp.models.participante import Participante
from SimpQuizApp.models.preguntas import Preguntas
from rest_framework import serializers

class ParticipacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participacion
        fields = ['ronda','puntaje_Ronda', 'preguntaId', 'participanteId']
    
    def to_representation(self, obj):
        participacion = Participacion.objects.get(id=obj.id)
        participante = Participante.objects.get(id=obj.participanteId_id)
        preguntas = Preguntas.objects.get(id=obj.preguntaId_id)
        return {
           'id': participacion.id,
           'ronda' : participacion.ronda,
           'puntaje_Ronda': participacion.puntaje_Ronda,
           'jugador': {
               'id': participante.id,
               'nickname': participante.nickname,
           },
           'pregunta':{
               'id' : preguntas.id,
               'pregunta': preguntas.pregunta,
           }
        }