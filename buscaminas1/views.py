from django.shortcuts import render, redirect
from .forms import TableroForm
from .models import Tablero


def crea_tablero(request):
    if request.method == 'POST':
        form = TableroForm(request.POST)
        if form.is_valid():
            dimension_x = form.cleaned_data['dimension_x']
            dimension_y = form.cleaned_data['dimension_y']

            tablero = Tablero.objects.create(dimension_x=dimension_x, dimension_y=dimension_y)

            return redirect('muestra_tablero', tablero_id=tablero.id)
    else:
        form = TableroForm()

    return render(request, 'crea_tablero.html', {'form': form})
