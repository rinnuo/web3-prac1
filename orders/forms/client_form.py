from django import forms
from orders.forms.form_utils import input_bootstrap_field
from orders.models import Client

class ClientForm(forms.ModelForm):
  name = forms.CharField(max_length=50, widget=input_bootstrap_field)
  nit = forms.CharField(max_length=20, required=False, widget=input_bootstrap_field)
  
  class Meta:
    model = Client
    fields = ['name', 'nit']