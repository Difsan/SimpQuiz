from SimpQuizApp.models.categorias import Categorias
from SimpQuizApp.models.respuestas import Respuestas
from SimpQuizApp.models.preguntas import Preguntas
from rest_framework import serializers

class RespuestasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Respuestas
        fields = ['respuesta', 'correcta', 'pre']

    def to_representation(self, obj):
        respuestas = Respuestas.objects.get(id=obj.id)
        preguntas = Preguntas.objects.get(id=obj.preg_Id_id) 
        return {
            'id' : respuestas.id,
            'respuesta' : respuestas.respuesta,
            'correcta' : respuestas.correcta,
            'pre' : {
                'id' : preguntas.id,
                'pregunta': preguntas.pregunta,
            }
        }