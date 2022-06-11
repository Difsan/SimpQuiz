from rest_framework import generics

from SimpQuizApp.models.participacion import Participacion
from SimpQuizApp.serializers.participacionSerializer import ParticipacionSerializer

# consular una participacion
class ParticipacionDetailView(generics.RetrieveAPIView):
    queryset = Participacion.objects.all()
    serializer_class =ParticipacionSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

#Todas las participaciones
class AllParticipacionesView(generics.ListAPIView):
    serializer_class = ParticipacionSerializer

    def get_queryset(self):
        queryset = Participacion.objects.all()
        return queryset

# Actualizar la participacion, me sirve para ir cambiando segun el sujeto logre avanzar
#cada vez q actualice tiene que ir todo el body del postman, cambiando solo lo que se quiere
class ActualizacionParticipacionView(generics.UpdateAPIView):
    queryset = Participacion.objects.all()
    serializer_class = ParticipacionSerializer

    def put(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

#Eliminar una participacion
class BorrarParticipacionView(generics.DestroyAPIView):
    queryset           = Participacion.objects.all()

    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)