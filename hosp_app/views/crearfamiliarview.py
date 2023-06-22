from urllib import request
from rest_framework import status,views
from rest_framework.response import Response

from hosp_app.serializers.Familiarserializers import familiarserializers
from hosp_app.models.Familiar import familiar


class Crearfamiliarview(views.APIView):
    def post (self, request, *args, **kwargs):
        serializer=familiarserializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Consultafamiliarview(views.APIView):

    def get(self, request, pk, format=None):
        snippet = familiar.objects.get(pk=pk)
        serializer = familiarserializers(snippet)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        snippet = familiar.objects.get(pk=pk)
        serializer = familiarserializers(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = familiar.objects.get(pk=pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)