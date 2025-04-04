from django.shortcuts import render, redirect
from orders.forms import OrderForm
from orders.models import Order


def order_list(request):
  orders = Order.objects.all()
  return render(request, 'orders/list.html', {'orders': orders})


def order_create(request):
  if request.method == 'POST':
    form = OrderForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('order_list')
  else:
    form = OrderForm()
  return render(request, 'orders/form.html', {'form': form})


def order_edit(request, id):
  order = Order.objects.get(id=id)
  if request.method == 'POST':
    form = OrderForm(request.POST, instance=order)
    if form.is_valid():
      form.save()
      return redirect('order_list')
  else:
    form = OrderForm(instance=order)
  return render(request, 'orders/form.html', {'form': form})


def order_delete(request, id):
  if request.method == 'GET':
    return redirect('order_list')
  order = Order.objects.get(id=id)
  order.delete()
  return redirect('order_list')
