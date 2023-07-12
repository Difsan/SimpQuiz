from django.contrib import admin
from django.urls import path
from SimpQuizApp import views
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="SimpQuiz API",
      default_version='v1',
      description="app to play quiz about The Simpson",
      terms_of_service="https://www.google.com/policies/terms/",
      #contact=openapi.Contact(email="contact@snippets.local"),
      #license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('participante/', views.ParticipanteCreateView.as_view()),
    path('participante/<int:pk>/', views.ParticipanteDetailView.as_view()),
    path('participante/filter/<str:nickname>/', views.FilterParticipanteView.as_view()),
    path('participante/all/', views.AllParticipantesView().as_view()),
    path('participante/update/<int:pk>/', views.ActualizarParticipanteView.as_view()),

    path('categorias/<int:pk>/', views.CategoriasDetailView().as_view()),
    path('categorias/all/', views.AllCategoriasView.as_view()),

    path('respuestas/<int:pk>/', views.RespuestasDetailView.as_view()),
    path('respuestas/filter/<int:preg_id>/', views.FilterRespuestasView.as_view()),

    path('preguntas/<int:pk>/', views.PreguntasDetailView.as_view()),
    path('preguntas/all/', views.AllPreguntasView.as_view()),
    path('preguntas/filter/<int:categ_id>/', views.FilterPreguntasView.as_view()),

    path('participacion/', views.ParticipacionCreateView.as_view()),
    path('participacion/<int:pk>/', views.ParticipacionDetailView.as_view() ),
    path('participacion/all/', views.AllParticipacionesView.as_view() ),
    path('participacion/update/<int:pk>/', views.ActualizacionParticipacionView.as_view()),
    path('participacion/remove/<int:pk>/', views.BorrarParticipacionView.as_view()),

    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
