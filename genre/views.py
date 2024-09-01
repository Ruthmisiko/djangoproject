from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return render(request,'hello.html',{})

def contact(request):
    return render(request,'contact.html',{})


def about(request):
    return render(request,'about.html',{})

def guard(request):
    return render(request,'guard.html',{})

def service(request):
    return render(request,'service.html',{})

# Create your views here.
