from SimpQuizApp.models.participante import Participante
from rest_framework import serializers

class ParticipanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participante
        fields = ['nickname', 'puntaje_Total']
    
    def to_representation(self, obj):
        participante = Participante.objects.get(id=obj.id)
        return {
            'id' : participante.id,
            'nickname': participante.nickname,
            'puntaje_Total': participante.puntaje_Total
        }