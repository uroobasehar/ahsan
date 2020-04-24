from django import forms
from app.models import *
from django_select2.forms import Select2MultipleWidget

class productForm(forms.ModelForm):
    class Meta:  
        model = product
        fields = "__all__"

class categoryForm(forms.ModelForm):
    class Meta:  
        model = product_category
        fields = "__all__"

class reviewForm(forms.ModelForm):
    class Meta:  
        model = review
        fields = "__all__"
  