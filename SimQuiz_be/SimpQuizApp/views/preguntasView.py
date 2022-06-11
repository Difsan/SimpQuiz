
from rest_framework import generics

from SimpQuizApp.models.preguntas import Preguntas
from SimpQuizApp.serializers.preguntasSerializer import PreguntasSerializer

# consular una pregunta
class PreguntasDetailView(generics.RetrieveAPIView):
    queryset = Preguntas.objects.all()
    serializer_class = PreguntasSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

#Todas las preguntas
class AllPreguntasView(generics.ListAPIView):
    serializer_class = PreguntasSerializer

    def get_queryset(self):
        queryset = Preguntas.objects.all()
        return queryset

# Preguntas filtradas por categoria
class FilterPreguntasView(generics.ListAPIView):
    serializer_class = PreguntasSerializer

    def get_queryset(self):
        queryset = Preguntas.objects.filter(categ_id_id=self.kwargs['categ_id'])
        return queryset
