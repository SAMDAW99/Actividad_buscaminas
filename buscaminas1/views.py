from django.shortcuts import render

from .forms import TableroForm


def welcome(request):
    return render(request, 'buscaminas1/index.html', {})


def crea_tablero(request):
    form = TableroForm()
    if request.method == 'GET':
        form = TableroForm(request.GET)
        if form.is_valid():
            columnas = form.cleaned_data['columnas']
            filas = form.cleaned_data['filas']
            return render(request, 'buscaminas1/mostrar_tablero.html', {'filas': filas, 'columnas':columnas,'rango_filas':range(filas), 'rango_columnas': range(columnas)})
    return render(request, 'buscaminas1/crea_tablero.html', {'form': form})
