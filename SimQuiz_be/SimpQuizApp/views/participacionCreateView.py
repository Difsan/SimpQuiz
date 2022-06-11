from rest_framework import generics, status
from rest_framework.response import Response
from SimpQuizApp.serializers.participacionSerializer import ParticipacionSerializer

class ParticipacionCreateView(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):
        serializer = ParticipacionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)