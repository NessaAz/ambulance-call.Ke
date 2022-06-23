from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

from .forms import *


def home(request):  
    context = {}
    
    return render(request, 'ambulanceapp/home.html', context)


def provider(request, template='ambulanceapp/provider.html'):
    if request.method == 'POST':
        form = AmbulanceproviderForm(request.POST)
        if form.is_valid():
            
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            
            user = User(username=username, email=email)
            user.set_password(password)
            user.save()
            
            return HttpResponseRedirect('/success/')
    else:
        form = AmbulanceproviderForm()

    return render(request, template, {'form':form})

