import json

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from SimpQuizApp.models import Participante, Categorias, Respuestas, Preguntas, Participacion
from SimpQuizApp.serializers import ParticipanteSerializer, CategoriasSerializer, RespuestasSerializer, PreguntasSerializer, ParticipacionSerializer

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
        parti = Participante.objects.create(nickname="user_test", puntaje_Total = 0)
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
        parti = Participante.objects.create(nickname="user_test", puntaje_Total = 0)
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
        parti = Participante.objects.create(nickname="user_test", puntaje_Total = 0)
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
        Categorias.objects.create(nivel = 6, puntaje = 6000)
        response = client.get('/categorias/all/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), (len(cate)+1))
    
    def test_categoriasDetailView(self):
        client = APIClient()
        cate = Categorias.objects.create(nivel = 6, puntaje = 6000)
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
        cate = Categorias.objects.create(nivel = 6, puntaje= 6000)

        pregu_all = list(Preguntas.objects.all())
        pregu_max_id = max(pregu_all, key=lambda x: x.id)
        pregu = Preguntas.objects.create(id = (pregu_max_id.id + 1), pregunta = "A la grande le puse?", categ_id = cate)
        
        respu_all = list(Respuestas.objects.all())
        respu_max_id = max(respu_all, key=lambda x: x.id)
        Respuestas.objects.create(id = (respu_max_id.id + 1),respuesta= "Cuca", preg_Id = pregu, correcta = True)
        Respuestas.objects.create(id = (respu_max_id.id + 2),respuesta= "Pepa", preg_Id = pregu, correcta = False)
        Respuestas.objects.create(id = (respu_max_id.id + 3),respuesta= "Lupe", preg_Id = pregu, correcta = False)
        Respuestas.objects.create(id = (respu_max_id.id + 4),respuesta= "Nena", preg_Id = pregu, correcta = False)
        respu = Respuestas.objects.filter(preg_Id = pregu)

        url = '/respuestas/filter/' + str(pregu.id) + '/'
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), (len(respu)))
    
    def test_respuestasDetailView(self):
        client = APIClient()
        cate = Categorias.objects.create(nivel = 6, puntaje= 6000)

        pregu_all = list(Preguntas.objects.all())
        pregu_max_id = max(pregu_all, key=lambda x: x.id)
        pregu = Preguntas.objects.create(id = (pregu_max_id.id + 1), pregunta = "A la grande le puse?", categ_id = cate)
        
        respu_all = list(Respuestas.objects.all())
        respu_max_id = max(respu_all, key=lambda x: x.id)
        respu = Respuestas.objects.create(id = (respu_max_id.id + 1),respuesta= "Cuca", preg_Id = pregu, correcta = True)
        respu_json = RespuestasSerializer(respu).data

        url = '/respuestas/' + str(respu.id) + '/'
        response = client.get(url)
        self.assertEqual(response.status_code, 200)        
        self.assertEqual(response.data, respu_json)
        self.assertEqual(response.data["id"], respu.id)
        self.assertEqual(response.data["respuesta"], respu.respuesta)
        self.assertEqual(response.data["pre"]["id"], respu.preg_Id.id)
        self.assertEqual(response.data["correcta"], respu.correcta)
    
    # Test preguntas   
    def test_allPreguntasView(self):
        client = APIClient()
        cate = Categorias.objects.create( nivel = 6, puntaje= 6000)

        pregu_all = list(Preguntas.objects.all())
        pregu_max_id = max(pregu_all, key=lambda x: x.id)
        Preguntas.objects.create(id = (pregu_max_id.id + 1), pregunta = "A la grande le puse?", categ_id = cate)
        
        response = client.get('/preguntas/all/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), (len(pregu_all)+1))
    
    def test_preguntasDetailView(self):
        client = APIClient()
        cate = Categorias.objects.create( nivel = 6, puntaje= 6000)

        pregu_all = list(Preguntas.objects.all())
        pregu_max_id = max(pregu_all, key=lambda x: x.id)
        pregu = Preguntas.objects.create(id = (pregu_max_id.id + 1), pregunta = "A la grande le puse?", categ_id = cate)
        pregu_json = PreguntasSerializer(pregu).data

        url = '/preguntas/' + str(pregu.id) + '/'
        response = client.get(url)
        self.assertEqual(response.status_code, 200)        
        self.assertEqual(response.data, pregu_json)
        self.assertEqual(response.data["pregunta"], pregu.pregunta)
        self.assertEqual(response.data["level"]["id"], cate.id)
    
    def test_filterPreguntasView(self):
        client = APIClient()
        cate = Categorias.objects.create( nivel = 6, puntaje= 6000)

        pregu_all = list(Preguntas.objects.all())
        pregu_max_id = max(pregu_all, key=lambda x: x.id)
        pregu = Preguntas.objects.create(id = (pregu_max_id.id + 1), pregunta = "A la grande le puse?", categ_id = cate)
        pregu_list = Preguntas.objects.filter(categ_id = cate)

        url = '/preguntas/filter/' + str(cate.id) + '/'
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), (len(pregu_list)))
    
    # Test para participacion
    def test_participacionCreateView(self):
        client = APIClient()
        cate = Categorias.objects.create( nivel = 6, puntaje= 6000)

        pregu_all = list(Preguntas.objects.all())
        pregu_max_id = max(pregu_all, key=lambda x: x.id)
        pregu = Preguntas.objects.create(id = (pregu_max_id.id + 1), pregunta = "A la grande le puse?", categ_id = cate)

        parti = Participante.objects.create(nickname="user_test", puntaje_Total = 0)

        response = client.post('/participacion/',
            {
                "ronda":"1",
                "participanteId": parti.id,
                "preguntaId": pregu.id,
                "puntaje_Ronda": 0
            },
            format = 'json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["ronda"], "1")
        self.assertEqual(response.data["jugador"]["id"], parti.id)
        self.assertEqual(response.data["pregunta"]["id"], pregu.id)
    
    def test_participacionDetailView(self):
        client = APIClient()
        cate = Categorias.objects.create( nivel = 6, puntaje= 6000)

        pregu_all = list(Preguntas.objects.all())
        pregu_max_id = max(pregu_all, key=lambda x: x.id)
        pregu = Preguntas.objects.create(id = (pregu_max_id.id + 1), pregunta = "A la grande le puse?", categ_id = cate)

        parti = Participante.objects.create(nickname="user_test", puntaje_Total = 0)

        all_participacion = list(Participacion.objects.all())
        obect_max_id = max(all_participacion, key=lambda x: x.id)
        partici = Participacion.objects.create(id =(obect_max_id.id + 1 ), ronda = 1, 
                                     preguntaId = pregu, participanteId = parti, puntaje_Ronda= 0)
        partici_json = ParticipacionSerializer(partici).data

        url = '/participacion/'+ str(partici.id) + '/'
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, partici_json)
        self.assertEqual(response.data["id"], partici.id)
    
    def test_allParticipacionesView(self):
        client = APIClient()
        cate = Categorias.objects.create( nivel = 6, puntaje= 6000)

        pregu_all = list(Preguntas.objects.all())
        pregu_max_id = max(pregu_all, key=lambda x: x.id)
        pregu = Preguntas.objects.create(id = (pregu_max_id.id + 1), pregunta = "A la grande le puse?", categ_id = cate)

        parti = Participante.objects.create(nickname="user_test", puntaje_Total = 0)

        all_participacion = list(Participacion.objects.all())
        obect_max_id = max(all_participacion, key=lambda x: x.id)
        Participacion.objects.create(id =(obect_max_id.id + 1 ), ronda = 1, 
                                     preguntaId = pregu, participanteId = parti, puntaje_Ronda= 0)
        
        response = client.get('/participacion/all/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), (len(all_participacion)+1))
    
    def test_actualizacionParticipacionView(self):
        client = APIClient()
        cate = Categorias.objects.create( nivel = 6, puntaje= 6000)

        pregu_all = list(Preguntas.objects.all())
        pregu_max_id = max(pregu_all, key=lambda x: x.id)
        pregu = Preguntas.objects.create(id = (pregu_max_id.id + 1), pregunta = "A la grande le puse?", categ_id = cate)

        parti = Participante.objects.create(nickname="user_test", puntaje_Total = 0)

        all_participacion = list(Participacion.objects.all())
        obect_max_id = max(all_participacion, key=lambda x: x.id)
        Participacion.objects.create(id =(obect_max_id.id + 1 ), ronda = 1, 
                                     preguntaId = pregu, participanteId = parti, puntaje_Ronda= 0)
        partici = Participacion.objects.get(id =(obect_max_id.id + 1 ))
        partici_json = ParticipacionSerializer(partici).data

        url = '/participacion/update/' + str(partici.id) + '/'
        response = client.put(url,
            {
                "id" : partici.id,
                "ronda":"3",
                "participanteId": parti.id,
                "preguntaId": pregu.id,
                "puntaje_Ronda": 1200
            }, 
            format = 'json')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.data, partici_json)
        self.assertNotEqual(response.data["ronda"], partici.ronda)
        self.assertNotEqual(response.data["puntaje_Ronda"], partici.puntaje_Ronda)
    
    def test_borrarParticipacionView(self):
        client = APIClient()
        cate = Categorias.objects.create( nivel = 6, puntaje= 6000)

        pregu_all = list(Preguntas.objects.all())
        pregu_max_id = max(pregu_all, key=lambda x: x.id)
        pregu = Preguntas.objects.create(id = (pregu_max_id.id + 1), pregunta = "A la grande le puse?", categ_id = cate)

        parti = Participante.objects.create(nickname="user_test", puntaje_Total = 0)

        partici = Participacion.objects.create(ronda = 1, 
                                     preguntaId = pregu, participanteId = parti, puntaje_Ronda= 0)
        partici_json = ParticipacionSerializer(partici).data

        url = '/participacion/remove/'+ str(partici.id) + '/'
        response = client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertNotEqual(response.data, partici_json)