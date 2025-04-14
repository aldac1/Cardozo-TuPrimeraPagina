from django.shortcuts import render, redirect
from tienda.models.ropa import Ropa
from tienda.forms.formulario_ropa import RopaForm

def ropa_list(request):
    ropa = Ropa.objects.all()
    return render(request, 'ropa_list.html', {'ropas': ropa})

def ropa_create(request):
    if request.method == 'POST':
        form = RopaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ropa_list')
    else:
        form = RopaForm()
    return render(request, 'ropa_form.html', {'form': form})

def ropa_update(request, ropa_id):
    prenda = Ropa.objects.get(id=ropa_id)
    if request.method == 'POST':
        form = RopaForm(request.POST, instance=prenda)
        if form.is_valid():
            form.save()
            return redirect('ropa_list')
    else:
        form = RopaForm(instance=prenda)
    return render(request, 'ropa_form.html', {'form': form})

def ropa_delete(request, ropa_id):
    prenda = Ropa.objects.get(id=ropa_id)
    prenda.delete()
    return redirect('ropa_list')
