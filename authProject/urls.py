"""authProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from hosp_app import views

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),

    path('user/', views.Crearusuarioview.as_view()),
    path('usuarioDetails/<int:pk>/', views.UsuarioDetailsview.as_view()),

    path('personal/', views.Crearpersonalview.as_view()),
    path('personalconsulta/<int:pk>/', views.Consultapersonalview.as_view()),

    path('paciente/', views.Crearpacienteview.as_view()),
    path('pacienteconsulta/<int:pk>/', views.Consultapacienteview.as_view()),

    path('familiar/', views.Crearfamiliarview.as_view()),
    path('familiarconsulta/<int:pk>/', views.Consultafamiliarview.as_view()),
]