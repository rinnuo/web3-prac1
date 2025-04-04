from django.shortcuts import render, redirect
from orders.forms import PaymentForm
from orders.models import Payment


def payment_list(request):
  payments = Payment.objects.all()
  return render(request, 'payments/list.html', {'payments': payments})


def payment_create(request):
  if request.method == 'POST':
    form = PaymentForm(request.POST)
    if form.is_valid():
      payment = form.save()
      payment.order.completed = True
      payment.order.save()
      return redirect('payment_list')
  else:
    form = PaymentForm()
  return render(request, 'payments/form.html', {'form': form})


def payment_edit(request, id):
  payment = Payment.objects.get(id=id)
  if request.method == 'POST':
    form = PaymentForm(request.POST, instance=payment)
    if form.is_valid():
      form.save()
      return redirect('payment_list')
  else:
    form = PaymentForm(instance=payment)
  return render(request, 'payments/form.html', {'form': form})


def payment_delete(request, id):
  if request.method == 'GET':
    return redirect('payment_list')
  payment = Payment.objects.get(id=id)
  payment.delete()
  return redirect('payment_list')
