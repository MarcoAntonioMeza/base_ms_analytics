from django.shortcuts import render,redirect
from django.urls import reverse
from direccion.forms import DireccionForm
from .forms import UsuarioCreationForm
from direccion.models import Estado

# Create your views here.
def index(request):
    return render(request, 'user/index.html')


#def crear_usuario(request):
#    if request.method == 'POST':
#        form = UsuarioCreationForm(request.POST, request.FILES)
#        if form.is_valid():
#            form.save()
#            return redirect(reverse('user_index'))  # Ajusta al nombre de tu URL para listar usuarios
#    else:
#        form = UsuarioCreationForm()
#
#    return render(request, 'user/create.html', {'form': form})


#def crear_usuario(request):
#    estados = Estado.objects.all()
#    if request.method == 'POST':
#        user_form = UsuarioCreationForm(request.POST)
#        direccion_form = DireccionForm(request.POST)
#
#        if user_form.is_valid() and direccion_form.is_valid():
#            usuario = user_form.save()
#            direccion = direccion_form.save(commit=False)
#            direccion.usuario = usuario  # Asociar la dirección con el usuario
#            direccion.save()
#            return redirect('user_index')
#    else:
#        user_form = UsuarioCreationForm()
#        direccion_form = DireccionForm()
#
#    return render(request, 'user/create.html', {
#        'user_form': user_form,
#        'direccion_form': direccion_form,
#        'estados': estados,
#    })

def crear_usuario(request):
    estados = Estado.objects.all()
    if request.method == 'POST':
        user_form = UsuarioCreationForm(request.POST)
        direccion_form = DireccionForm(request.POST)

        if user_form.is_valid() and direccion_form.is_valid():
            usuario = user_form.save()
            direccion = direccion_form.save(commit=False)
            direccion.usuario = usuario  # Asociar la dirección con el usuario
            direccion.save()
            return redirect('user_index')
    else:
        user_form = UsuarioCreationForm()
        direccion_form = DireccionForm()

    return render(request, 'user/create.html', {
        'user_form': user_form,
        'direccion_form': direccion_form,
        'estados': estados,
    })