from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django import template
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import render_to_string
from django.template import loader
from django.urls import reverse
from direccion.models import Estado
from apps.clientes.models import Cliente
from .models import Solicitud
from django.http import Http404
from xhtml2pdf import pisa


def index(request):
    estados = Estado.objects.all()

    if request.method == 'POST':
        # Extrae los datos del formulario
        consumo = request.POST.get('consumo')
        pago = request.POST.get('pago')
        estado_id = request.POST.get('estado')
        cantidad_energia_ahorrada = request.POST.get('cantidad_energia_ahorrada')
        name = request.POST.get('name')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        print(consumo, pago, estado_id, cantidad_energia_ahorrada, name, email, telefono)

        
        #Obtén el estado por su ID
        estado_ob = get_object_or_404(Estado,id=estado_id)
        client = Cliente.objects.filter(email=email).first()
        if client == None:
            client = Cliente(nombres=name, apellidos='', telefono=telefono, email=email)
            client.save()
       
        solicitud = Solicitud(
            consumo_kwh=consumo,
            pago=pago,
            estado=estado_ob,  # Usamos el ID del estado
            cantidad_energia_ahorrada=cantidad_energia_ahorrada,
            cliente=client,  # Aquí debes asignar el cliente correspondiente
        )
        
        
        solicitud.save()
        messages.success(request, '¡El PDF ha sido enviado a su correo electrónico!')
        return redirect('detalle_simulacion', id=solicitud.id)
        
           

        # Contexto para el PDF
        context = {
            'nombre': 'Juan Pérez',
            'estado': 'Activo',
            'consumo': 500,
            'cantidad_energia_ahorrada': 30,
            'pago': 120.50,
        }

        # Renderizar el HTML a partir de la plantilla
        html_string = render_to_string('pdf/simulador/preCotizacion.html', context)

        # Crear el PDF usando xhtml2pdf
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="reporte.pdf"'

        # Usar pisa para convertir el HTML a PDF
        pisa_status = pisa.CreatePDF(html_string, dest=response)

        if pisa_status.err:
            return HttpResponse('Error al generar el PDF', status=400)

        # Después de generar el PDF, agregamos un mensaje
        
        messages.success(request, '¡El PDF ha sido enviado a su correo electrónico!')

        # Redirigir al usuario a la misma página para que vea el mensaje
        return redirect('simulador_index')

    return render(request, 'simulador/index.html', {'estados': estados})


def detail_simulacion(request, id):
    solicitud = get_object_or_404(Solicitud, id=id)
    return render(request, 'simulador/resultados.html', {'solicitud': solicitud})


def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('simulador/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:
        
        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))
    except Http404:
        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
    
   
        
