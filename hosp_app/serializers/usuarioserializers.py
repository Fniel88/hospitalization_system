from dataclasses import field
from pyexpat import model
from hosp_app.models.usuario import usuario
from rest_framework import serializers

class Usuarioserializer(serializers.ModelSerializer):

    class Meta:
        model = usuario
        fields = ('id_username','username','password','perfil','nombre','apellidos','telefono','genero')