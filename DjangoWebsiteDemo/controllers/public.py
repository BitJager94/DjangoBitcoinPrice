from django.shortcuts import render
#from myapp.models import Product


def index(request):
#    products = Product.objects.all()
    return render(request, 'index.html')