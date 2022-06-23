from django import forms
from django.contrib.auth.forms import UserCreationForm
from . models import *


class AddressMixin(forms.ModelForm):
    class Meta:
        model = Ambulanceprovider
        fields = ('address_one', 'address_two', 'county', 'town',)
        widgets = {
            'address_one': forms.TextInput(attrs={'class':'form-control'}),
            'address_two': forms.TextInput(attrs={'class':'form-control'}),
            'city': forms.TextInput(attrs={'class':'form-control'}),
            'state': forms.TextInput(attrs={'class':'form-control'}),
        }    
        


class AmbulanceproviderForm(AddressMixin, UserCreationForm):
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'type':'password'}))
    password2 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'type':'password'}))
    
    class Meta:
        model = User
        fields = ("username",)
