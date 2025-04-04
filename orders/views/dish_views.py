from django.shortcuts import render, redirect
from orders.forms import DishForm
from orders.models import Dish


def dish_list(request):
  dishes = Dish.objects.all()
  return render(request, 'dishes/list.html', {'dishes': dishes})


def dish_create(request):
  if request.method == 'POST':
    form = DishForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('dish_list')
  else:
    form = DishForm()
  return render(request, 'dishes/form.html', {'form': form})


def dish_edit(request, id):
  dish = Dish.objects.get(id=id)
  if request.method == 'POST':
    form = DishForm(request.POST, instance=dish)
    if form.is_valid():
      form.save()
      return redirect('dish_list')
  else:
    form = DishForm(instance=dish)
  return render(request, 'dishes/form.html', {'form': form})


def dish_delete(request, id):
  if request.method == 'GET':
    return redirect('dish_list')
  dish = Dish.objects.get(id=id)
  dish.delete()
  return redirect('dish_list')
