import json

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from SimpQuizApp.models import Participante, Categorias, Respuestas, Preguntas
from SimpQuizApp.serializers import ParticipanteSerializer, CategoriasSerializer, RespuestasSerializer

# Create your tests here.
class TestAPI(TestCase):

    # Test de participantes URL
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
        parti = list(Participante.objects.all())

        Participante.objects.create(nickname="user_test", puntaje_Total = 0)
        Participante.objects.create(nickname="user_test2", puntaje_Total = 1500)
        response = client.get('/participante/all/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), (len(parti)+2))
    
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
    
    # Test Categorias URL
    def test_allCategoriasView(self):
        client = APIClient()
        cate = list(Categorias.objects.all())
        Categorias.objects.create(id = (len(cate)+1),  nivel = 6, puntaje = 6000)
        response = client.get('/categorias/all/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), (len(cate)+1))
    
    def test_categoriasDetailView(self):
        client = APIClient()
        all_cate = list(Categorias.objects.all())
        Categorias.objects.create(id = (len(all_cate)+1),  nivel = 6, puntaje = 6000)
        cate = Categorias.objects.get(id = (len(all_cate)+1))
        parti_json = CategoriasSerializer(cate).data

        url = '/categorias/'+ str(cate.id) + '/'
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, parti_json)
        self.assertEqual(response.data["id"], cate.id)
        self.assertEqual(response.data["nivel"], cate.nivel)
        self.assertEqual(response.data["puntaje"], cate.puntaje)
    
    # Test Respuestas URL
    def test_filterRespuestasView(self):
        client = APIClient()
        response1 = list(Categorias.objects.all())
        Categorias.objects.create(id = (len(response1) + 1 ), nivel = 6, puntaje= 6000)
        cate = Categorias.objects.get(id = (len(response1) + 1 ))

        response2 = list(Preguntas.objects.all())
        Preguntas.objects.create(id = (len(response2) + 1 ), pregunta = "A la grande le puse?", categ_id = cate)
        pregu = Preguntas.objects.get(id = (len(response2) + 1 ))

        response3 = list(Respuestas.objects.all())
        Respuestas.objects.create(id = (len(response3) + 1 ),respuesta= "Cuca", preg_Id = pregu, correcta = True)
        Respuestas.objects.create(id = (len(response3) + 2 ),respuesta= "Pepa", preg_Id = pregu, correcta = False)
        Respuestas.objects.create(id = (len(response3) + 3 ),respuesta= "Lupe", preg_Id = pregu, correcta = False)
        Respuestas.objects.create(id = (len(response3) + 4 ),respuesta= "Nena", preg_Id = pregu, correcta = False)
        respu = Respuestas.objects.filter(preg_Id = pregu)

        url = '/respuestas/filter/' + str(pregu.id) + '/'
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), (len(respu)))
    
    def test_respuestasDetailView(self):
        client = APIClient()
        response1 = list(Categorias.objects.all())
        Categorias.objects.create(id = (len(response1) + 1 ), nivel = 6, puntaje= 6000)
        cate = Categorias.objects.get(id = (len(response1) + 1 ))

        response2 = list(Preguntas.objects.all())
        Preguntas.objects.create(id = (len(response2) + 1 ), pregunta = "A la grande le puse?", categ_id = cate)
        pregu = Preguntas.objects.get(id = (len(response2) + 1 ))

        response3 = list(Respuestas.objects.all())
        Respuestas.objects.create(id = (len(response3) + 1 ),respuesta= "Cuca", preg_Id = pregu, correcta = True)
        respu = Respuestas.objects.get(id = (len(response3) + 1 ))
        respu_json = RespuestasSerializer(respu).data

        url = '/respuestas/' + str(respu.id) + '/'
        response = client.get(url)
        self.assertEqual(response.status_code, 200)        
        self.assertEqual(response.data, respu_json)
        self.assertEqual(response.data["id"], respu.id)
        self.assertEqual(response.data["respuesta"], respu.respuesta)
        self.assertEqual(response.data["pre"]["id"], respu.preg_Id.id)
        self.assertEqual(response.data["correcta"], respu.correcta)
        
        