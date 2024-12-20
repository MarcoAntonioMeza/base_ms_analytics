from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django import forms

class UsuarioCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'nombre', 'segundo_nombre', 'apellido_paterno', 'apellido_materno', 
                  'profile_picture', 'access_to_app', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'access_to_app':
                # Estiliza el checkbox como un switch
                field.widget.attrs['class'] = 'form-check-input custom-switch-input'
            else:
                # Aplica la clase form-control a otros campos
                field.widget.attrs['class'] = 'form-control'
            if field_name == 'segundo_nombre':
                # Establece que 'segundo_nombre' no sea obligatorio
                field.required = False
