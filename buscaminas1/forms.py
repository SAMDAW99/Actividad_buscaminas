from django import forms


class TableroForm(forms.Form):
    dimension_x = forms.IntegerField(label='Ancho del tablero')
    dimension_y = forms.IntegerField(label='Alto del tablero')
    # Agrega otros campos del formulario si es necesario
