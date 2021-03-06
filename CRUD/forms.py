from django import forms
from .models import customerDetails

class registrationForm(forms.ModelForm):
    class Meta:
        model = customerDetails
        fields = ['Assignto', 'address', 'number']
        widgets = {
            'Assignto' : forms.TextInput(attrs={'class': 'form-control'}),
            'address' : forms.TextInput(attrs={'class': 'form-control'}),
            'number' : forms.TextInput(attrs={'class': 'form-control'})
        }