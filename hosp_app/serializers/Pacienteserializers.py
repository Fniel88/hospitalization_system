from dataclasses import field
from pyexpat import model
from hosp_app.models import Paciente
from hosp_app.models.Paciente import paciente
from rest_framework import serializers

class pacienteserializer(serializers.ModelSerializer):

    class Meta:
        model = paciente
        fields = ('id_UserName','direccion','ciudad','fecha_nacimiento')