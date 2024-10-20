from django.shortcuts import render
from .models import Product
# Create your views here.

def product_details_view(request):
    obj = Product.objects.get(id=1)
    data = {
        'title': obj.title,
        'description': obj.description,
        'price' : obj.price,
        'color': obj.color,
        'sammary': obj.sammary,
        'featured' : obj.featured   
    }
    return render(request,'product/detailes.html',data)
