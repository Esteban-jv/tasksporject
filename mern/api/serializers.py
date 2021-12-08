from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Proyecto, Tarea # Or just the models you need

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','is_active']

class ProyectoSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
        model = Proyecto
        fields = '__all__'

class TareaSerializer(serializers.ModelSerializer):
    proyecto = serializers.PrimaryKeyRelatedField(queryset=Proyecto.objects.all())
    class Meta:
        model = Tarea
        fields = '__all__'