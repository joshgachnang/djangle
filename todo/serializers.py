from rest_framework import serializers

from form_api import forms
from todo.models import Todo


class TodoSerializer(serializers.Serializer):
    class Meta:
        model = Todo
        fields = ('title', 'description')


forms.api.register(TodoSerializer)