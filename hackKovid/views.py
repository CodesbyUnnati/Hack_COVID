from django.shortcuts import render, HttpResponse
from .models import Product

# Create your views here.

def home(request):
    return render(request, 'index.html')

def store(request):
    item = Product.objects.values()
    allProds = {'item': item}
    return render(request, 'store.html', allProds)

def guide(request):
    return render(request, 'guidelines.html')

def cart(request):
    return render(request, 'cart.html')

def thankyou(request):
    return render(request, 'thankyou.html')

def checkout(request):
    return render(request, 'checkout.html')

def products(request, stri):
    allprods = Product.objects.values()
    catprods = Product.objects.filter(id=stri)
    allprod = {'allprod': allprods, 'catprod': catprods}
    return render(request, 'shop-single.html', allprod)