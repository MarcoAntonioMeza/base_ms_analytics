from django.shortcuts import render,redirect,get_object_or_404
from django.db.models import Q
from django.http import JsonResponse
from django.core.paginator import Paginator
from .models import Cliente
from datetime import datetime
from django.utils.dateformat import format

#==================================================================
#                               MAIN CRUD 
#==================================================================
def index(request):
    return render(request, 'clientes/index.html')

def create(request):
    pass
    #return render(request, 'clientes/create.html')
def view(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    return render(request, 'clientes/view.html', {'cliente': cliente})

def update(request, id):
    pass
    #return render(request, 'clientes/update.html')
def delete(request, id):
    pass
    #return render(request, 'clientes/delete.html')



  
#==================================================================
#                            LIST TABLES
#==================================================================
def index_list_ajax(request):
    draw = int(request.GET.get('draw', 1))
    start = int(request.GET.get('start', 0))
    length = int(request.GET.get('length', 10))
    search_value = request.GET.get('search[value]', '')

    # Filtrado por búsqueda
    clients = Cliente.objects.all()
    if search_value:
       clients = clients.filter(
        Q(nombres__icontains=search_value) |
        #Q(apellido_paterno__icontains=search_value) |
        #Q(email__icontains=search_value)|
        Q(id__icontains=search_value)
        #Q(username__icontains=search_value)
    )
    # Paginación
    paginator = Paginator(clients, length)
    page_number = (start // length) + 1
    page_obj = paginator.get_page(page_number)

    # Serializar datos
    data = [
        {
            "id": s.id,
            "full_name": f"{s.nombres}  {s.apellido_paterno} {s.apellido_materno}",
            "phone": str(s.telefono),
            "phone2": str(s.telefono2),
            'tipo': s.get_tipo_display(),
            'estado': s.get_estado_display(),
            
            "email": str(s.email),
            #"created_at": s.created_at,
            "created_at": format(s.created_at, 'd-m-Y h:i:s'),
            #"created_by": str(s.created_by.username) if s.created_by else "",
        }
        for s in page_obj
    ]

    return JsonResponse({
        "draw": draw,
        "recordsTotal": paginator.count,
        "recordsFiltered": paginator.count,
        "data": data
    })

# Create your views here.
