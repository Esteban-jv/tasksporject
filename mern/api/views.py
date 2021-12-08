from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, ProyectoSerializer, TareaSerializer # or the Serializers you need
from .models import * # or the models you need

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import check_password

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework import status

from django.core.exceptions import ObjectDoesNotExist

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
        return Response(f'No existe una cuenta para {username}',status=status.HTTP_401_UNAUTHORIZED)

    pwd_valid = check_password(password,user.password)
    if not pwd_valid:
        return Response('Contraseña incorrecta',status=status.HTTP_401_UNAUTHORIZED)

    token, created = Token.objects.get_or_create(user=user)
    print(token.key)
    return Response(token.key)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def projectsUsuario(request, id):
    # Search user
    # Search projects by user
    projects = Proyecto.objects.filter(user_id=id)
    serializer = ProyectoSerializer(projects, many=True)
    # print(projects,serializer)
    # Serializer data
    # Return that data
    return Response(serializer.data, status=status.HTTP_200_OK)

# CRUD usuarios

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def usersGet(request, id):
    try:
        user = User.objects.get(id=id)
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({'detail': 'Usuario no encontrado', 'exception':None}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def usersCreate(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def usersUpdate(request, id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response({'detail': 'Usuario no encontrado', 'exception': None}, status=status.HTTP_400_BAD_REQUEST)
    serializer = UserSerializer(instance=user, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def usersDelete(request, id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response({'detail': 'Usuario no encontrado', 'exception': None}, status=status.HTTP_400_BAD_REQUEST)
    user.delete()

    return Response({'detail':'Usuario eliminado'}, status=status.HTTP_200_OK)

# CRUD proyectos

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def projectsGet(request, id):
    try:
        project = Proyecto.objects.get(id=id)
        serializer = ProyectoSerializer(project, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Proyecto.DoesNotExist:
        return Response({'detail': 'Proyecto no encontrado', 'exception':None}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def projectsCreate(request):
    serializer = ProyectoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def projectsUpdate(request, id):
    try:
        project = Proyecto.objects.get(id=id)
    except Proyecto.DoesNotExist:
        return Response({'detail': 'Proyecto no encontrado', 'exception': None}, status=status.HTTP_400_BAD_REQUEST)
    serializer = ProyectoSerializer(instance=project, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def projectsDelete(request, id):
    try:
        project = Proyecto.objects.get(id=id)
    except Proyecto.DoesNotExist:
        return Response({'detail': 'Proyecto no encontrado', 'exception': None}, status=status.HTTP_400_BAD_REQUEST)
    project.delete()

    return Response({'detail':'Proyecto eliminado'}, status=status.HTTP_200_OK)

# CRUD tareas

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def tasksProject(request, id):
    tasks = Tarea.objects.filter(proyecto_id=id)
    serializer = TareaSerializer(tasks, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def tasksGet(request, id):
    try:
        tarea = Tarea.objects.get(id=id)
        serializer = TareaSerializer(tarea, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Tarea.DoesNotExist:
        return Response({'detail': 'Tarea no encontrada', 'exception':None}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def tasksCreate(request):
    serializer = TareaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def tasksUpdate(request, id):
    try:
        tarea = Tarea.objects.get(id=id)
    except Tarea.DoesNotExist:
        return Response({'detail': 'Tarea no encontrada', 'exception': None}, status=status.HTTP_400_BAD_REQUEST)
    serializer = TareaSerializer(instance=tarea, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def tasksDelete(request, id):
    try:
        tarea = Tarea.objects.get(id=id)
    except Tarea.DoesNotExist:
        return Response({'detail': 'tarea no encontrada', 'exception': None}, status=status.HTTP_400_BAD_REQUEST)
    tarea.delete()

    return Response({'detail':'Tarea eliminada'}, status=status.HTTP_200_OK)
