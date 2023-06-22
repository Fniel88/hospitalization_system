from urllib import request
from rest_framework import status,views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainSerializer 

from hosp_app.serializers.usuarioserializers import Usuarioserializer


class Crearusuarioview(views.APIView):
    def post (self, request, *args, **kwargs):
        serializer=Usuarioserializer (data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()


        tokenData ={
            "username":request.data["username"],
            "password":request.data["password"]
        }

        tokenSerializer = TokenObtainSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)

        return Response(tokenSerializer.validate_data, status=status.HTTP_201_CREATED)


