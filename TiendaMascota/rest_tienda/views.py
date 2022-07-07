from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import *
from .serializers import *
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
# Create your views here.


@api_view(['GET', 'POST'])
def lista_productos(request):
    if request.method == "GET":
        list = Producto.objects.all()
        serializer= ProductoSerializer(list, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = ProductoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def detalle_producto(request, id):
    try:
        producto= Producto.objects.get(idProducto=id)
    except Producto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer= ProductoSerializer(producto)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProductoSerializer(producto, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def producto_read_all(request):
    if request.method == 'GET':
        list = Producto.objects.all()
        serializer = ProductoSerializer(list, many=True)
        return Response(serializer.data)

#@permission_classes((IsAuthenticated,))
class producto_create(APIView):
    def post(self, request, format=None):
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class producto_update(APIView):
    def put(self, request, format=None):
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.update()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    data = JSONParser().parse(request)
    username = data['username']
    password = data['password']
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response("Usuario inválido")
    password_valida = check_password(password, user.password)
    if not password_valida:
        return Response("Contraseña incorrecta")
    token, created = Token.objects.get_or_create(user=user)
    print(f"Este es el token creado: '{token.key}'")
    return Response(token.key)

@csrf_exempt
@api_view(['DELETE'])
def vehiculo_delete(request, id):
    if request.method == 'DELETE':
        try:
            Producto.objects.get(idProducto=id).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Producto.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)