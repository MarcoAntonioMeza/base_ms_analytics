from django import forms
from .models import Cliente
from direccion.models import CodigoPostal, Estado, Municipio, Colonia
from .models import DireccionClientes
#from apps.usuario.models import Direccion

class ClienteForm(forms.ModelForm):
    
    class Meta:
        model = Cliente
        fields = ['nombres', 'apellido_paterno', 'apellido_materno', 'telefono','telefono2', 'email', 'tipo', 'estado', 'giro', 'fecha_nacimiento']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'tipo' or field_name == 'estado':
                field.widget.attrs['class'] = 'form-control select2-container select2-selection--single'
            else:
                field.widget.attrs['class'] = 'form-control'
            if field_name == 'telefono2':
                field.required = False
            if field_name == 'giro':
                field.required = False
            if field_name == 'fecha_nacimiento':
                field.required = False



class DireccionForm(forms.ModelForm):
    class Meta:
        model = DireccionClientes
        fields = ['estado', 'municipio', 'codigo_postal', 'colonia', 'calle', 'numero_exterior', 'numero_interior']
        
    # Campo extra para la búsqueda del código postal (ahora es opcional)
    codigo_postal = forms.CharField(max_length=7, label="Código Postal", required=False)
    municipio = forms.ModelChoiceField(queryset=Municipio.objects.none(), required=False)
    colonia = forms.ModelChoiceField(queryset=Colonia.objects.none(), required=False)
    #codigo_postal = forms.ModelChoiceField(queryset=CodigoPostal.objects.all(), required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['estado'].queryset = Estado.objects.all()
        # Si hay un estado seleccionado, actualizar los municipios y colonias
        estado = self.initial.get('estado') or self.data.get('estado')
        if estado:
            self.fields['municipio'].queryset = Municipio.objects.filter(estado=estado)

        municipio = self.initial.get('municipio') or self.data.get('municipio')
        if municipio:
            self.fields['colonia'].queryset = Colonia.objects.filter(municipio=municipio)
         # Si hay una instancia de direccion cargada, poner el codigo postal en el campo
        #if self.instance and self.instance.codigo_postal:
        #    self.fields['codigo_postal'].initial = self.instance.codigo_postal.codigo_postal
        
            

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

        self.fields['estado'].widget.attrs.update({'class': 'form-control select2-container select2-selection--single', 'data-placeholder': '-- SELECCIONA UN ESTADO --'})
        self.fields['municipio'].widget.attrs.update({'class': 'form-control select2-container select2-selection--single', 'data-placeholder': '-- SELECCIONA UN MUNICIPIO --'})
        self.fields['colonia'].widget.attrs.update({'class': 'form-control select2-container select2-selection--single', 'data-placeholder': '-- SELECCIONA UNA COLONIA --'})

        # Inicializar 'calle' como no obligatorio por defecto
        self.fields['calle'].required = False
        self.fields['estado'].required = False
        self.fields['municipio'].required = False
        self.fields['colonia'].required = False
        self.fields['codigo_postal'].required = False
    
    
    def clean_codigo_postal(self):
        codigo_postal = self.cleaned_data.get('codigo_postal')

        # Si no hay código postal, no hacer nada
        if not codigo_postal:
            return None

        # Buscar el código postal por su valor
        try:
            codigo = CodigoPostal.objects.get(codigo_postal=codigo_postal)
            self.instance.codigo_postal = codigo
            return codigo  # Devolver la instancia de CodigoPostal
        except CodigoPostal.DoesNotExist:
            raise forms.ValidationError("El código postal no es válido.")
    
    def clean_municipio(self):
        municipio = self.cleaned_data.get('municipio')
        if municipio and municipio not in self.fields['municipio'].queryset:
            raise forms.ValidationError("Seleccione un municipio válido.")
        return municipio

    def clean_colonia(self):
        colonia = self.cleaned_data.get('colonia')
        if colonia and colonia not in self.fields['colonia'].queryset:
            raise forms.ValidationError("Seleccione una colonia válida.")
        return colonia