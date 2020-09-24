from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, 'index.html')

def store(request):
    return render(request, 'store.html')

def guide(request):
    return render(request, 'guidelines.html')