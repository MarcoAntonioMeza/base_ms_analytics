from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from direccion.forms import DireccionForm

from .forms import UsuarioCreationForm
from direccion.models import Estado
from .models import Usuario, Direccion

#from apps.usuario.forms import UsuarioCreationForm, DireccionForm


# Create your views here.
def index(request):
    return render(request, 'user/index.html')



def crear_usuario(request):
    estados = Estado.objects.all()
    
    if request.method == 'POST':
        # Crear los formularios con los datos del POST
        user_form = UsuarioCreationForm(request.POST)
        direccion_form = DireccionForm(request.POST)

        print(request.POST)

        # Verificar si ambos formularios son válidos
        if user_form.is_valid() and direccion_form.is_valid():
            usuario = user_form.save()  # Guardar el usuario
            direccion = direccion_form.save(commit=False)  # No guardar aún la dirección

            # Si no se proporcionó un código postal, lo dejamos como None
            if  direccion_form.cleaned_data.get('estado') and direccion_form.cleaned_data.get('municipio') and direccion_form.cleaned_data.get('colonia'):
                #direccion.codigo_postal = None  # Asignar None si no hay código postal
                direccion.usuario = usuario  # Asociar la dirección al usuario
                direccion.save()  # Guardar la dirección

            return redirect('user_index')  # Redirigir al índice de usuarios u otra página
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
    # Obtener el usuario
    usuario = get_object_or_404(Usuario, id=id)
    
    # Verificar si el usuario tiene una dirección
    try:
        direccion = Direccion.objects.get(usuario=usuario)
    except Direccion.DoesNotExist:
        # Si el usuario no tiene dirección, crear una nueva dirección vacía
        direccion = Direccion(usuario=usuario)

    # Cargar los formularios con los datos existentes
    if request.method == 'POST':
        print(request.POST)
        # Los formularios de usuario y dirección con los datos enviados
        user_form = UsuarioCreationForm(request.POST, instance=usuario)
        direccion_form = DireccionForm(request.POST, instance=direccion)

        # Verificar si ambos formularios son válidos
        if user_form.is_valid() and direccion_form.is_valid():
            # Guardar los cambios en el usuario y la dirección
            usuario = user_form.save()  # Guardar usuario actualizado
            direccion = direccion_form.save()  # Guardar dirección actualizada

            return redirect('user_index')  # Redirigir al índice de usuarios u otra página
        else:
            # Si los formularios no son válidos, mostrar los errores
            return render(request, 'user/update.html', {
                'user_form': user_form,
                'direccion_form': direccion_form,
                'usuario': usuario,
            })
    else:
        # Si no es un POST, crear los formularios con los datos del usuario y dirección existentes
        user_form = UsuarioCreationForm(instance=usuario)
        direccion_form = DireccionForm(instance=direccion)

    return render(request, 'user/update.html', {
        'user_form': user_form,
        'direccion_form': direccion_form,
        'usuario': usuario,
    })