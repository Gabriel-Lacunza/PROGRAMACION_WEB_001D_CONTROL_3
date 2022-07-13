from django.shortcuts import redirect
from django.contrib.auth.models import User
from .models import *
from .views import *

def comprar_producto (request):
    