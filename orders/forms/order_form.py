from django import forms
from orders.forms.form_utils import select_bootstrap_field
from orders.models import Order, Table, Waiter, Dish

class OrderForm(forms.ModelForm):
  table = forms.ModelChoiceField(queryset=Table.objects.exclude(id__in=Order.objects.filter(completed=False).values('table_id')), widget=select_bootstrap_field)
  waiter = forms.ModelChoiceField(queryset=Waiter.objects.exclude(id__in=Order.objects.filter(completed=False).values('waiter_id')), widget=select_bootstrap_field)
  dishes = forms.ModelMultipleChoiceField(queryset=Dish.objects.all(), widget=forms.CheckboxSelectMultiple)

  class Meta:
    model = Order
    fields = ['table', 'waiter', 'dishes']