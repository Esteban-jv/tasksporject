from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import * # or the Serializers you need
from .models import * # or the models you need

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import check_password

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework import status

# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def apiOverview(request):
    api_urls = {
        'List': '/users/list/',
        'Detail View': '/users/detail/<int:id>/',
        'Create': '/users/create/',
        'Update': '/users/update/<int:id>/',
        'Delete': '/users/delete/<int:id>/',
    }
    return Response(api_urls)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def usersList(request):
    models = User.objects.all()
    serializer = UserSerializer(models, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def login(request):

    username = request.data.get('username','')
    password = request.data.get('password')

    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response('Usuario inválido')

    pwd_valid = check_password(password,user.password)
    if not pwd_valid:
        return Response('Contraseña inválida')

    token, created = Token.objects.get_or_create(user=user)
    print(token.key)
    return Response(token.key)
