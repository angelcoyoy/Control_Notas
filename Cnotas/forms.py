from django import forms
from .models import Grado, Materia

class GradoForm(forms.ModelForm):
    class Meta:
        model = Grado
        fields = ('nombre', 'semestre', 'seccion', 'jornada', 'anio', 'materias')

        def __init__ (self, *args, **kwargs):
            super(GradoForm, self).__init__(*args, **kwargs)
            self.fields["materias"].widget = forms.widgets.CheckboxSelectMultiple()
            self.fields["materias"].help_text = "Ingrese las materias asignadas al grado"
            self.fields["materias"].queryset = Materia.objects.all()

            fields = [
            'nombre',
            'semestre',
            'seccion',
            'jornada',
            'anio',
            'materias',
        ]
        labels = {
            'nombre': 'Nombre',
            'semestre': 'Semetre',
            'seccion': 'Secion',
            'jornada': 'jornada',
            'anio': 'anio',
            'materias': 'materias',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'semestre': forms.TextInput(attrs={'class':'form-control'}),
            'seccion': forms.TextInput(attrs={'class':'form-control'}),
            'jorndas': forms.TextInput(attrs={'class':'form-control'}),
            'anio': forms.TextInput(attrs={'class':'form-control'}),
            'materias' : forms.CheckboxSelectMultiple(),
        }
