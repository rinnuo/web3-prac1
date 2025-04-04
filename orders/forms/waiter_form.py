from django import forms
from orders.forms.form_utils import input_bootstrap_field
from orders.models import Waiter

class WaiterForm(forms.ModelForm):
  first_name = forms.CharField(max_length=50, widget=input_bootstrap_field)
  last_name = forms.CharField(max_length=50, widget=input_bootstrap_field)
  phone = forms.CharField(max_length=20, widget=input_bootstrap_field)
  
  class Meta:
    model = Waiter
    fields = ['first_name', 'last_name', 'phone']