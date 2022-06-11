from django.conf import settings
from rest_framework import generics

from SimpQuizApp.models.categorias import Categorias
from SimpQuizApp.serializers.categoriasSerializer import CategoriasSerializer

# una categoria no mas
class CategoriasDetailView(generics.RetrieveAPIView):
    queryset = Categorias.objects.all()
    serializer_class = CategoriasSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

#Todas las categorias
class AllCategoriasView(generics.ListAPIView):
    serializer_class = CategoriasSerializer

    def get_queryset(self):
        queryset = Categorias.objects.all()
        return queryset