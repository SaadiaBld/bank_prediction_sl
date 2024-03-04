from django import forms
from .models import UserRegister

class UserForm(forms.ModelForm):
    class Meta:
        model = UserRegister
        fields = '__all__'

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'border p-2 rounded-md'}),
            'last_name': forms.TextInput(attrs={'class': 'border p-2 rounded-md'}),
            'email': forms.EmailInput(attrs={'class': 'border p-2 rounded-md'}),
        }
        
