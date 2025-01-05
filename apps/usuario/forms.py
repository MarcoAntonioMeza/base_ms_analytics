from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django import forms
from django.contrib.auth.models import  Group,Permission
#==================================================================
#                            USER FORM
#==================================================================

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
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if Usuario.objects.filter(username=username).exclude(id=self.instance.id).exists():
            raise forms.ValidationError("Ya existe un usuario con este nombre de usuario.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Usuario.objects.filter(email=email).exclude(id=self.instance.id).exists():
            raise forms.ValidationError("Ya existe un usuario con este correo electrónico.")
        return email
    
#==================================================================
#                            LOGIN
#==================================================================
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control' , 'placeholder': 'Usuario'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}))