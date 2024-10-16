from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_view(request,*args, **kwargs):
    # print(args,kwargs)
    # print(request.user)
    return render(request ,'home.html',{} )

def contact_page(request):

    return render(request , 'contacr.html',{})

def about_page(request):
    
    return render(request , 'about.html',{})

def social_page(request):
    
    return render(request , 'social.html',{})
