# Django Rest Framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Local Models
from task import serializers, models

class TaskAPiView(APIView):
    """ API de tareas """
    serializer_class = serializers.TasksSerializer

    def get(self, request, format=None, *args, **kwargs):
        objects = models.Tasks.objects.all()
        serializer = self.serializer_class(objects, many=True)
        return Response(serializer.data)


    def post(self, request):
        """ Crea nuevo Usuario """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'status': status.HTTP_201_CREATED})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


class TaskApiViewDetail(APIView):
    """ Modificación y eliminación de tareas """
    serializer_class = serializers.TasksSerializer

    def get_object(self, pk):
        try:
            return models.Tasks.objects.get(pk=pk)
        except models.Tasks.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = self.serializer_class(post, data=request.data)
        if serializer.is_valid():
            serializer.save()   
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)