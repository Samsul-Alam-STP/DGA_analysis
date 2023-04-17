from django import forms
from .models import DGA_Values

class DGA_form(forms.ModelForm):
    class Meta:
        model = DGA_Values
        fields = '__all__'


class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email')
    subject = forms.CharField(label='Subject', max_length=200)
    message = forms.CharField(widget=forms.Textarea)