from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Proyecto Model
class Proyecto(models.Model):
    nombre = models.CharField(max_length=200, null=False, default='') # Needs to take default out of here
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=False)

    def __str__(self):
        return f'Proyecto: {self.nombre}'

# Tareas model
class Tarea(models.Model):
    nombre = models.CharField(max_length=200, null=False) # Needs to take default out of here
    completed = models.BooleanField(default=False)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.DO_NOTHING, null=False)

    def __str__(self):
        return f'Tarea: {self.nombre}, estatus: {self.completed}'
