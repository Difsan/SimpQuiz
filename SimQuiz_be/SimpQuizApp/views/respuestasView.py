from rest_framework import generics

from SimpQuizApp.models.respuestas import Respuestas
from SimpQuizApp.serializers.respuestasSerializer import RespuestasSerializer

# consular una respuesta
class RespuestasDetailView(generics.RetrieveAPIView):
    queryset = Respuestas.objects.all()
    serializer_class = RespuestasSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

#Todas las Respuestas
class AllRespuestasView(generics.ListAPIView):
    serializer_class = RespuestasSerializer

    def get_queryset(self):
        queryset = Respuestas.objects.all()
        return queryset

# Respuestas filtradas por Pregunta
class FilterRespuestasView(generics.ListAPIView):
    serializer_class = RespuestasSerializer

    def get_queryset(self):
        queryset = Respuestas.objects.filter(preg_Id_id=self.kwargs['preg_id'])
        return queryset
