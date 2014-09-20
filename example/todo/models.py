from django.db import models
from django.contrib import admin
from rest_framework import serializers
from rest_framework import viewsets

from djangle import form_api

CATEGORIES = (('Do Now', 'Do Now'), ('Later', 'later'))


class Todo(models.Model):
    title = models.CharField(max_length=255,
                             help_text='What do you need to do?')
    description = models.TextField(help_text='How are you going to do it?',
    )
    due_date = models.DateField(blank=True, null=True, default=None)
    link = models.URLField(blank=True, null=True, default=None)
    category = models.CharField(choices=CATEGORIES, max_length=32,
                                default='Do Now')


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('title', 'description', 'due_date', 'link', 'category')


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


admin.site.register(Todo)
form_api.api.register('todo', TodoSerializer)
