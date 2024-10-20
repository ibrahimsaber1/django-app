from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_view(request,*args, **kwargs):
    # print(args,kwargs)
    # print(request.user)
    return render(request ,'home.html',{} )

def contact_page(request):
    contact_data = {
        'name': 'Ibrahim Saber',
        'age': '24',
        'sex' : 'male',
        'job' : 'software engneer',
        'fields' : ['data analysis','data science','medical rep.']
    }

    return render(request , 'contacr.html',contact_data)

def about_page(request):
    my_context = {
        "title": "our number",
        "num":"01023456789",
        "note": "bro dont call us"
    }
    return render(request , 'about.html',my_context)

def social_page(request):
    
    return render(request , 'social.html',{})
