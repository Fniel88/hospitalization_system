from dataclasses import fields
from hosp_app.models.PSalud import Personal_Salud
from rest_framework import serializers

class psaludserializer(serializers.ModelSerializer):
    class Meta:
        model= Personal_Salud
        fields = ('id_UserName','rol','especialidad')

        