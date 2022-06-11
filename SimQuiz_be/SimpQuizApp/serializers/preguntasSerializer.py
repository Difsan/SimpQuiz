from SimpQuizApp.models.preguntas import Preguntas
from SimpQuizApp.models.categorias import Categorias
from rest_framework import serializers

class PreguntasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preguntas
        fields = ['pregunta', 'level']
    
    def to_representation(self, obj):
        preguntas = Preguntas.objects.get(id=obj.id)
        categorias = Categorias.objects.get(id=obj.categ_id_id)
        return{
            'id' : preguntas.id,
            'pregunta': preguntas.pregunta,
            'level' : {
                'id' : categorias.id,
                'nivel' : categorias.nivel,
                'puntaje': categorias.puntaje,
            } 
        }