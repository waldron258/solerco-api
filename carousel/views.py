from django.shortcuts import render, redirect
import os
import uuid
from django.core.files.uploadedfile import SimpleUploadedFile

from decimal import Decimal  # Asegúrate de importar Decimal
from django.contrib import messages  # Para usar mensajes flash
from django.core.exceptions import ObjectDoesNotExist

# Para el informe (Reporte) Excel
import pandas as pd

import json

import logging

from django.utils import timezone
# from openpyxl import Workbook  # Para generar el informe en excel
from django.http import HttpResponse, JsonResponse

from django.shortcuts import get_object_or_404

from django.http import JsonResponse
from .models import Carousel # Importando el modelo de carousel
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

def carousel_create(request):
    if request.method == 'POST':
        # Aquí deberías validar los datos del request
        carousel = Carousel(title=request.POST['title'], description=request.POST['description'], image=request.FILES['image'])
        carousel.save()
        return JsonResponse({'mensaje': 'Carousel created successfully'})


def create_carousel(request):
    if request.method == 'POST':
        """ 
        Iterando a través de todos los elementos en el diccionario request.POST, 
        que contiene los datos enviados a través del método POST, e imprime cada par clave-valor en la consola
        for key, value in request.POST.items():
            print(f'{key}: {value}')
        """
        title = request.POST.get('title')
        description = request.POST.get('description')

        # Obtén la imagen del formulario
        image = request.FILES.get('image')

        if image:
            image = generate_unique_filename(image)

        # Procesa los datos y guarda en la base de datos
        carousel = Carousel(
            title=title,
            description=description,
            image=image,
        )
        carousel.save()

        # messages.success(
        #     request, f"Felicitaciones, el empleado {nombre} fue registrado correctamente 😉")


def generate_unique_filename(file):
    extension = os.path.splitext(file.name)[1]
    unique_name = f'{uuid.uuid4()}{extension}'
    return SimpleUploadedFile(unique_name, file.read())