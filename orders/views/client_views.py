from django.shortcuts import render, redirect
from orders.forms import ClientForm
from orders.models import Client


def client_list(request):
  clients = Client.objects.all()
  return render(request, 'clients/list.html', {'clients': clients})


def client_create(request):
  if request.method == 'POST':
    form = ClientForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('client_list')
  else:
    form = ClientForm()
  return render(request, 'clients/form.html', {'form': form})


def client_edit(request, id):
  client = Client.objects.get(id = id)
  if request.method == 'POST':
    form = ClientForm(request.POST, instance=client)
    if form.is_valid():
      form.save()
      return redirect('client_list')
  else:
    form = ClientForm(instance=client)
  return render(request, 'clients/form.html', {'form': form})


def client_delete(request, id):
  if request.method == 'GET':
    return redirect('client_list')
  client = Client.objects.get(id = id)
  client.delete()
  return redirect('client_list')