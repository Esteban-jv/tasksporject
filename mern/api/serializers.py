from rest_framework import serializers
from django.contrib.auth.models import User
from .models import * # Or just the models you need

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','is_active']