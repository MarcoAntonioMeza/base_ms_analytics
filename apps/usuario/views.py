from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from django.db.models import Q
from django.http import JsonResponse
from django.core.paginator import Paginator
from direccion.forms import DireccionForm
from datetime import datetime

from .forms import UsuarioCreationForm
from direccion.models import Estado
from .models import Usuario, Direccion

#from apps.usuario.forms import UsuarioCreationForm, DireccionForm


# Create your views here.
def index(request):
    return render(request, 'user/index.html')

def view_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    #print(usuario.profile_picture.url)
    # Verificar si el usuario tiene una dirección
    try:
        direccion = Direccion.objects.get(usuario=usuario)
    except Direccion.DoesNotExist:
        direccion = Direccion(usuario=usuario)
        
    return render(request, 'user/view.html', {'usuario': usuario, 'direccion': direccion})

def crear_usuario(request):
    estados = Estado.objects.all()
    if request.method == 'POST':
        # Crear los formularios con los datos del POST
        user_form = UsuarioCreationForm(request.POST, request.FILES)
        direccion_form = DireccionForm(request.POST)

        #print(request.POST)

        # Verificar si ambos formularios son válidos
        if user_form.is_valid() and direccion_form.is_valid():
            usuario = user_form.save(commit=False)  # Guardar el usuario
            grupo = user_form.cleaned_data['grupos']
            permisos = user_form.cleaned_data['permisos']
            usuario.save()  # Guardar el usuario
            if grupo:
                usuario.groups.add(grupo)
            if permisos:
                usuario.user_permissions.set(permisos)
                
            direccion = direccion_form.save(commit=False)  # No guardar aún la dirección

            # Si no se proporcionó un código postal, lo dejamos como None
            if  direccion_form.cleaned_data.get('estado') and direccion_form.cleaned_data.get('municipio') and direccion_form.cleaned_data.get('colonia'):
                #direccion.codigo_postal = None  # Asignar None si no hay código postal
                direccion.usuario = usuario  # Asociar la dirección al usuario
                direccion.save()  # Guardar la dirección

            return redirect('user_view',id=usuario.id)  # Redirigir al índice de usuarios u otra página
        else:
            # Si algún formulario no es válido, mostramos los errores en el template
            return render(request, 'user/create.html', {
                'user_form': user_form,
                'direccion_form': direccion_form,
                'estados': estados,
            })
    else:
        # Si no es un POST, crear formularios vacíos
        user_form = UsuarioCreationForm()
        direccion_form = DireccionForm()

    return render(request, 'user/create.html', {
        'user_form': user_form,
        'direccion_form': direccion_form,
        'estados': estados,
    })


def update_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    # Verificar si el usuario tiene una dirección
    try:
        direccion = Direccion.objects.get(usuario=usuario)
    except Direccion.DoesNotExist:
        # Si el usuario no tiene dirección, crear una nueva dirección vacía
        direccion = Direccion(usuario=usuario)

    # Cargar los formularios con los datos existentes
    if request.method == 'POST':
        #print(request.POST)
        # Los formularios de usuario y dirección con los datos enviados
        user_form = UsuarioCreationForm(request.POST, request.FILES,instance=usuario)
        direccion_form = DireccionForm(request.POST, instance=direccion)

        # Verificar si ambos formularios son válidos
        if user_form.is_valid() and direccion_form.is_valid():
            # Guardar los cambios en el usuario y la dirección
            usuario = user_form.save()  # Guardar usuario actualizado
            grupo = user_form.cleaned_data['grupos']
            if grupo:
                usuario.groups.set(user_form.cleaned_data['grupos'])
                
            # Asignar los permisos seleccionados
            permisos = user_form.cleaned_data['permisos']
            if permisos:
                usuario.user_permissions.set(permisos)
                
            if  direccion_form.cleaned_data.get('estado') and direccion_form.cleaned_data.get('municipio') and direccion_form.cleaned_data.get('colonia'):
                #direccion.codigo_postal = None  # Asignar None si no hay código postal
                direccion.usuario = usuario  # Asociar la dirección al usuario
                #direccion.save()
                direccion = direccion_form.save()  # Guardar dirección actualizada

            return redirect('user_view',id=usuario.id)  # Redirigir al índice de usuarios u otra página
        else:
            # Si los formularios no son válidos, mostrar los errores
            return render(request, 'user/update.html', {
                'user_form': user_form,
                'direccion_form': direccion_form,
                'usuario': usuario,
            })
    else:
        # Si no es un POST, crear los formularios con los datos del usuario y dirección existentes
        user_form = UsuarioCreationForm(instance=usuario,initial={'grupos': usuario.groups.all(),
                                                                  'permisos': usuario.user_permissions.all()})
        direccion_form = DireccionForm(instance=direccion)

    return render(request, 'user/update.html', {
        'user_form': user_form,
        'direccion_form': direccion_form,
        'usuario': usuario,
    })
    
    
    
#==================================================================
#                            LIST TABLES
#==================================================================
def index_list_ajax(request):
    draw = int(request.GET.get('draw', 1))
    start = int(request.GET.get('start', 0))
    length = int(request.GET.get('length', 10))
    search_value = request.GET.get('search[value]', '')

    # Filtrado por búsqueda
    uesers = Usuario.objects.all()
    if search_value:
       uesers = uesers.filter(
        Q(nombre__icontains=search_value) |
        Q(apellido_paterno__icontains=search_value) |
        #Q(email__icontains=search_value)|
        Q(id__icontains=search_value)|
        Q(username__icontains=search_value)
    )
    # Paginación
    paginator = Paginator(uesers, length)
    page_number = (start // length) + 1
    page_obj = paginator.get_page(page_number)

    # Serializar datos
    data = [
        {
            "id": s.id,
            "usuario": str(s.username),
            "full_name": f"{s.nombre} {s.segundo_nombre} {s.apellido_paterno}",  # Asume que tienes 'nombre' y 'apellido' en el modelo
            "email": str(s.email),
            "created_at": datetime.fromtimestamp(s.created_at).strftime("%Y-%m-%d %H:%M:%S") if s.created_at else None,
            "created_by": str(s.created_by.username) if s.created_by else "",
        }
        for s in page_obj
    ]

    return JsonResponse({
        "draw": draw,
        "recordsTotal": paginator.count,
        "recordsFiltered": paginator.count,
        "data": data
    })