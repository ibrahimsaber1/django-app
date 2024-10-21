from django.shortcuts import render
from .models import Product
from .forms import ProductForm
# Create your views here.----------------------------- :)

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    data = {
        'form':form
    }
    return render(request,'products/create.html',data)


def product_details_view(request):
    obj = Product.objects.get(id=1)
    # data = {
    #     'title': obj.title,
    #     'description': obj.description,
    #     'price' : obj.price,
    #     'color': obj.color,
    #     'sammary': obj.sammary,
    #     'featured' : obj.featured   
    # }
    data = {
        'object':obj
    }
    return render(request,'products/detailes.html',data)
