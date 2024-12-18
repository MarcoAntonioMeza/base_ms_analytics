from django import forms
from .models import CodigoPostal, Estado, Municipio, Colonia
from apps.usuario.models import Direccion

class DireccionForm(forms.ModelForm):
    class Meta:
        model = Direccion
        fields = ['estado', 'municipio', 'codigo_postal', 'colonia', 'calle', 'numero_exterior', 'numero_interior']

    # Campo extra para la búsqueda del código postal
    codigo_postal = forms.CharField(max_length=10, label="Código Postal", required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['estado'].queryset = Estado.objects.all()
        self.fields['municipio'].queryset = Municipio.objects.none()
        self.fields['colonia'].queryset = Colonia.objects.none()
        for field_name, field in self.fields.items():          
            field.widget.attrs['class'] = 'form-control'


    def clean_codigo_postal(self):
        codigo_postal = self.cleaned_data.get('codigo_postal')
        try:
            # Buscar la instancia de CodigoPostal correspondiente
            codigo = CodigoPostal.objects.get(codigo_postal=codigo_postal)
        
            # Obtener la colonia asociada al código postal
            colonia = Colonia.objects.filter(codigo_postal=codigo).first()
        
            if colonia:
                # Obtener el municipio a partir de la colonia
                municipio = colonia.municipio
                estado = municipio.estado
        
                # Asignar la instancia de CodigoPostal al formulario
                self.instance.codigo_postal = codigo  # Asegúrate de asignar la instancia, no solo la cadena
                self.instance.estado = estado
                self.instance.municipio = municipio
        
                # Filtrar los municipios y colonias disponibles
                self.fields['municipio'].queryset = Municipio.objects.filter(estado=estado)
                self.fields['colonia'].queryset = Colonia.objects.filter(codigo_postal=codigo)
        
                return codigo  # Devolvemos la instancia de CodigoPostal
            else:
                raise forms.ValidationError("No se encontró una colonia para este código postal.")
        except CodigoPostal.DoesNotExist:
            raise forms.ValidationError("El código postal no es válido.")
