import json

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from SimpQuizApp.models import Participante
from SimpQuizApp.serializers import ParticipanteSerializer

# Create your tests here.
class TestAPI(TestCase):

    def test_participanteCreateView(self):
        client = APIClient()
        response = client.post('/participante/',
            {
                "nickname": "user_test",
                "puntaje_Total": 0
            },
            format = 'json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["nickname"], "user_test")
        self.assertEqual(response.data["puntaje_Total"], 0)

    

    def test_participanteDetailView(self):
        client = APIClient()
        Participante.objects.create(nickname="user_test", puntaje_Total = 0)
        parti = Participante.objects.get(nickname="user_test")
        parti_json = ParticipanteSerializer(parti).data

        url = '/participante/'+ str(parti.id) + '/'
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, parti_json)
        self.assertEqual(response.data["id"], parti.id)
        self.assertEqual(response.data["nickname"], parti.nickname)
        self.assertEqual(response.data["puntaje_Total"], parti.puntaje_Total)
    
    def test_filterParticipanteView(self):
        client = APIClient()

        Participante.objects.create(nickname="user_test", puntaje_Total = 0)
        parti = Participante.objects.get(nickname="user_test")
        parti_json = ParticipanteSerializer(parti).data

        url = '/participante/filter/' + str(parti.nickname) + '/'
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0], parti_json)
        self.assertEqual(response.data[0]["id"], parti.id)
        self.assertEqual(response.data[0]["nickname"], parti.nickname)
        self.assertEqual(response.data[0]["puntaje_Total"], parti.puntaje_Total)
    
    def test_allParticipanteView(self):
        client = APIClient()
        response1 = client.get('/participante/all/')
        Participante.objects.create(nickname="user_test", puntaje_Total = 0)
        Participante.objects.create(nickname="user_test2", puntaje_Total = 1500)
        response = client.get('/participante/all/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), (len(response1.json())+2))
    
    def test_actualizarParticipanteView(self):
        client = APIClient()
        Participante.objects.create(nickname="user_test", puntaje_Total = 0)
        parti = Participante.objects.get(nickname="user_test")
        parti_json = ParticipanteSerializer(parti).data

        url = '/participante/update/' + str(parti.id) + '/'
        response = client.put(url,
            {
                "id": parti.id,
                "nickname": "user_test3",
                "puntaje_Total": 1500
            },
            format = 'json')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.data, parti_json)
        self.assertNotEqual(response.data["nickname"], parti.nickname)
        self.assertNotEqual(response.data["puntaje_Total"], parti.puntaje_Total)