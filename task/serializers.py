# Django Rest Framework
from rest_framework import serializers

# Local Models
from task.models import Tasks

class TasksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tasks
        fields = ('id', 'username', 'name', 'description', 'attached_file')