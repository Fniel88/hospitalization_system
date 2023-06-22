from dataclasses import fields
from hosp_app.models.Familiar import familiar
from rest_framework import serializers

class familiarserializers(serializers.ModelSerializer):
    class Meta:
        model= familiar
        fields = ('id_UserName ','parentesco','correo')