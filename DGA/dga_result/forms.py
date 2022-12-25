from django import forms
from .models import DGA_Values

class DGA_form(forms.ModelForm):
    class Meta:
        model = DGA_Values
        fields = '__all__'