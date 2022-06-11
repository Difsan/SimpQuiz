from SimpQuizApp.models.categorias import Categorias
from rest_framework import serializers

class CategoriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorias
        fields = ['nivel', 'puntaje']

    def to_representation(self, obj):
        categorias = Categorias.objects.get(id=obj.id)
        return{
            'id' : categorias.id,
            'nivel' : categorias.nivel,
            'puntaje': categorias.puntaje,
        }