from django import forms
from orders.forms.form_utils import input_bootstrap_field
from orders.models import Table

class TableForm(forms.ModelForm):
  number = forms.IntegerField(widget=input_bootstrap_field)
  
  class Meta:
    model = Table
    fields = ['number']