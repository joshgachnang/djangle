from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField()
    description = models.TextField()
