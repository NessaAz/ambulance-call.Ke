from django.shortcuts import render

def home(request):  
    context = {}
    
    return render(request, 'ambulanceapp/home.html', context)