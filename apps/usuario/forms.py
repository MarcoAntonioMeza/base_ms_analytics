from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django import forms
from django.contrib.auth.models import  Group,Permission

class UsuarioCreationForm(UserCreationForm):
  
    grupos = forms.ModelMultipleChoiceField(
        queryset=Group.objects.all(),  # Obtiene todos los grupos
        required=False,  # Puede ser opcional
        widget=forms.SelectMultiple(attrs={'class': 'form-control select2'}),  # Usando select2 para la interfaz
    )
    # Campo para seleccionar permisos
    permisos = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.all(),  # Obtener todos los permisos
        required=False,  # Puede ser opcional
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}),  # Selección múltiple
    )
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'nombre', 'segundo_nombre', 'apellido_paterno', 'apellido_materno', 
                  'profile_picture', 'access_to_app', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'access_to_app':
                field.widget.attrs['class'] = 'form-check-input custom-switch-input'
            else:
                field.widget.attrs['class'] = 'form-control'
            if field_name == 'segundo_nombre':
                field.required = False
            if field_name == 'profile_picture':
                field.required = False
                
                
    def clean_profile_picture(self):
        picture = self.cleaned_data.get('profile_picture')
        if not picture:
            return None  
        return picture