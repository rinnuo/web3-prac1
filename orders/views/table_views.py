from django.shortcuts import render, redirect
from orders.forms import TableForm
from orders.models import Table


def table_list(request):
  tables = Table.objects.all()
  return render(request, 'tables/list.html', {'tables': tables})


def table_create(request):
  if request.method == 'POST':
    form = TableForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('table_list')
  else:
    form = TableForm()
  return render(request, 'tables/form.html', {'form': form})


def table_edit(request, id):
  table = Table.objects.get(id=id)
  if request.method == 'POST':
    form = TableForm(request.POST, instance=table)
    if form.is_valid():
      form.save()
      return redirect('table_list')
  else:
    form = TableForm(instance=table)
  return render(request, 'tables/form.html', {'form': form})


def table_delete(request, id):
  if request.method == 'GET':
    return redirect('table_list')
  table = Table.objects.get(id=id)
  table.delete()
  return redirect('table_list')
