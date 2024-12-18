from django.shortcuts import render
from django.http import JsonResponse
from .models import CodigoPostal, Municipio, Colonia
from django.http import JsonResponse
from .models import CodigoPostal, Municipio, Colonia

def buscar_direccion(request):
    codigo_postal = request.GET.get('codigo_postal')
    estado_id = request.GET.get('estado_id')
    municipio_id = request.GET.get('municipio_id')

    municipios = []
    colonias = []

    # Buscar por código postal
    if codigo_postal:
        try:
            codigo = CodigoPostal.objects.get(codigo_postal=codigo_postal)
            colonias = Colonia.objects.filter(codigo_postal=codigo)
            municipios = Municipio.objects.filter(id__in=colonias.values('municipio'))
        except CodigoPostal.DoesNotExist:
            return JsonResponse({'municipios': [], 'colonias': []})

    # Buscar por estado
    elif estado_id:
        municipios = Municipio.objects.filter(estado_id=estado_id)

    # Buscar por municipio
    elif municipio_id:
        colonias = Colonia.objects.filter(municipio_id=municipio_id)

    # Preparar los datos para la respuesta
    municipios_data = [{'id': municipio.id, 'nombre': municipio.nombre} for municipio in municipios]
    colonias_data = [{'id': colonia.id, 'd_asenta': colonia.d_asenta} for colonia in colonias]

    return JsonResponse({'municipios': municipios_data, 'colonias': colonias_data})
