from django.conf import settings
from rest_framework import generics


from SimpQuizApp.models.participante import Participante
from SimpQuizApp.serializers.participanteSerializer import ParticipanteSerializer

class ParticipanteDetailView(generics.RetrieveAPIView):
    queryset = Participante.objects.all()
    serializer_class = ParticipanteSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

# Participante filtrado por nickname
class FilterParticipanteView(generics.ListAPIView):
    serializer_class = ParticipanteSerializer

    def get_queryset(self):
        queryset = Participante.objects.filter(nickname=self.kwargs['nickname'])
        return queryset

#Todos los participantes
class AllParticipantesView(generics.ListAPIView):
    serializer_class = ParticipanteSerializer

    def get_queryset(self):
        queryset = Participante.objects.all()
        return queryset

#Actualizar participante
class ActualizarParticipanteView(generics.UpdateAPIView):
    queryset = Participante.objects.all()
    serializer_class = ParticipanteSerializer

    def put(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
