from urllib import request
from rest_framework import status,views
from rest_framework.response import Response


from hosp_app.serializers.Pacienteserializers import pacienteserializer
from hosp_app.models.Paciente import paciente

class Crearpacienteview(views.APIView):
    def post (self, request, *args, **kwargs):
        serializer=pacienteserializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Consultapacienteview(views.APIView):

    def get(self, request, pk, format=None):
        snippet = paciente.objects.get(pk=pk)
        serializer = pacienteserializer(snippet)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        snippet = paciente.objects.get(pk=pk)
        serializer = pacienteserializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = paciente.objects.get(pk=pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


