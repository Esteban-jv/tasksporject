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
    projects = Proyecto.objects.all()
    serializer = ProyectoSerializer(projects, many=True)
    # print(projects,serializer)
    # Serializer data
    # Return that data
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def projectsGet(request, id):
    project = Proyecto.objects.get(id=id)
    serializer = ProyectoSerializer(project, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)

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

'''
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def projectCreate(request):
    if request.method == 'POST':
        formaPersona = PersonaForm(request.POST)
        # Validar formulario
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('index')
    else:
        formaPersona = PersonaForm()
    return render(request, 'personas/nuevo.html', {
        'formaPersona':formaPersona,
    })'''