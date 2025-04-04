from django.shortcuts import render, redirect
from orders.forms import WaiterForm
from orders.models import Waiter


def waiter_list(request):
  waiters = Waiter.objects.all()
  return render(request, 'waiters/list.html', {'waiters': waiters})


def waiter_create(request):
  if request.method == 'POST':
    form = WaiterForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('waiter_list')
  else:
    form = WaiterForm()
  return render(request, 'waiters/form.html', {'form': form})


def waiter_edit(request, id):
  waiter = Waiter.objects.get(id=id)
  if request.method == 'POST':
    form = WaiterForm(request.POST, instance=waiter)
    if form.is_valid():
      form.save()
      return redirect('waiter_list')
  else:
    form = WaiterForm(instance=waiter)
  return render(request, 'waiters/form.html', {'form': form})


def waiter_delete(request, id):
  if request.method == 'GET':
    return redirect('waiter_list')
  waiter = Waiter.objects.get(id=id)
  waiter.delete()
  return redirect('waiter_list')
