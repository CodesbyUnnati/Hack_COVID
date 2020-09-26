from django.shortcuts import render, HttpResponse
from .models import Product, Order

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

def thankyou(request, methods = ["GET", "POST"]):
    if request.method == 'POST':
        country = request.POST.get('countryinput')
        itemsJson = request.POST.get('itemsJson')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        address = request.POST.get('address')
        state = request.POST.get('state')
        zipcode = request.POST.get('zip')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        amount = request.POST.get('amount')
        order = Order(itemsJson=itemsJson, FirstName=fname, LastName=lname, email=email, address=address,
                       state=state, postNumber=zipcode, phone=phone, amount=amount, country=country)
        order.save()
        return render(request, 'thankyou.html')

def checkout(request):
    return render(request, 'checkout.html')

def products(request, stri):
    allprods = Product.objects.values()
    catprods = Product.objects.filter(id=stri)
    allprod = {'allprod': allprods, 'catprod': catprods}
    return render(request, 'shop-single.html', allprod)

    # itemsJson = models.AutoField
    # country = models.CharField(max_length=50)
    # FirstName = models.CharField(max_length=30)
    # LastName = models.CharField(max_length=30)
    # address = models.CharField(max_length=50)
    # state = models.CharField(max_length=20)
    # postNumber = models.IntegerField()
    # email = models.CharField(max_length=20)
    # phone = models.CharField(max_length=20)