from django.db import models
from rest_framework import serializers
from rest_framework import viewsets

from django_angular_forms import form_api


class Todo(models.Model):
    title = models.CharField(max_length=255,
                             help_text='What do you need to do?')
    description = models.TextField(help_text='How are you going to do it?')
    due_date = models.DateTimeField()


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('title', 'description', 'due_date')


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


form_api.api.register('todo', TodoSerializer)
