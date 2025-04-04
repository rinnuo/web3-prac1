from django import forms
from orders.forms.form_utils import input_bootstrap_field
from orders.models import Dish

class DishForm(forms.ModelForm):
  name = forms.CharField(max_length=50, widget=input_bootstrap_field)
  description = forms.CharField(required=False, widget=input_bootstrap_field)
  
  class Meta:
    model = Dish
    fields = ['name', 'description']