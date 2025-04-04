from django import forms
from orders.forms.form_utils import select_bootstrap_field
from orders.models import Payment, Order, Client

class PaymentForm(forms.ModelForm):
  order = forms.ModelChoiceField(queryset=Order.objects.filter(completed=False), widget=select_bootstrap_field)
  client = forms.ModelChoiceField(queryset=Client.objects.all(), widget=select_bootstrap_field)
  
  class Meta:
    model = Payment
    fields = ['order', 'client']