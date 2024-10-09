from django.shortcuts import render

# Create your views here.
def verLista(request): 
    return render(request, 'index.html')