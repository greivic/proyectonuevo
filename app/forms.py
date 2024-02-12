from django.forms import ModelForm
from app.models import Instrumento

class InstrumentoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['placeholder'] = 'Introduzca el nombre'
        self.fields['color'].widget.attrs['placeholder'] = 'Introduzca el color'

        self.fields['nombre'].widget.attrs['class'] = 'form-control'
        self.fields['color'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = Instrumento
        fields = '__all__'