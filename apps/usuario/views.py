from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import UsuarioCreationForm

# Create your views here.
def index(request):
    return render(request, 'user/index.html')


def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('user_index'))  # Ajusta al nombre de tu URL para listar usuarios
    else:
        form = UsuarioCreationForm()

    return render(request, 'user/create.html', {'form': form})