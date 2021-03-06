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




class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('name', 'description', 'address_one',
                  'address_two', 'county', 'town', 'phone',
        )
        widgets = {
            'name': forms.TextInput(
                attrs={ 'placeholder':'Company', 'class':'col-md-8 form-control'  }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder':'Enter description,response time and scope of service',
                    'class':'form-control'
                }
            ),
            'address_one': forms.TextInput(
                attrs={
                    'placeholder':'Physical Address:ABC Building etc..',
                    'class':'gi-form-addr form-control'
                }
            ),
            'address_two': forms.TextInput(
                attrs={
                    'placeholder':'Geographical area of service',
                    'class':'gi-form-addr form-control'
                }
            ),
            'county': forms.TextInput(
                attrs={
                    'placeholder':'County',
                    'class':'gi-form-addr form-control'
                }
            ),
            'town': forms.TextInput(
                attrs={
                    'placeholder':'Town',
                    'class':'gi-form-addr form-control'
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'placeholder':'Phone number' ,
                    'class':'gi-form-addr form-control'
                }
            ),
        }