from rest_framework import serializers

from todo.models import Todo


class TodoSerializer(serializers.Serializer):
    class Meta:
        model = Todo
        fields = ('title', 'description', 'due_date')