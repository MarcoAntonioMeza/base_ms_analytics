from django.shortcuts import render
from django import template
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import render_to_string
from django.template import loader
from django.urls import reverse
from direccion.models import Estado
from apps.clientes.models import Cliente
from .models import Solicitud
#import pdfkit
from xhtml2pdf import pisa
#import weasyprint


# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.template.loader import render_to_string
from xhtml2pdf import pisa
from .models import Estado, Cliente, Solicitud

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

        try:
            # Obtén el estado por su ID
            estado_ob = Estado.objects.get(id=estado_id)
        except Estado.DoesNotExist:
            # Si el estado no existe, redirige o muestra un error
            return HttpResponse('Estado no encontrado', status=404)

        # Crear el cliente
        client = Cliente(nombres=name, apellidos='', telefono=telefono, email=email)
        client.save()

        # Crear la solicitud
        solicitud = Solicitud(
            consumo_kwh=consumo,
            pago=pago,
            estado=estado_ob,  # Usamos el ID del estado
            cantidad_energia_ahorrada=cantidad_energia_ahorrada,
            cliente=client,  # Aquí debes asignar el cliente correspondiente
        )
        solicitud.save()

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
        pass
        #html_template = loader.get_template('home/page-404.html')
        #return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
