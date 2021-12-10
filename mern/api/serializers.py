from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Proyecto, Tarea # Or just the models you need

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','first_name','last_name','username','password','email','is_active']

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        # last_login = some_python_var # Must be now by default
        user.save()
        return user

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