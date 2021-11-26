from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def dashboard(request,name):
    return render(request,'dashboard.html',{'name':name})

def home(request):
    return render(request,'dashboard.html',{'name':'this is home page','title':'Dashboard'})

def login(request):
    return render(request,'login.html',{'title':'Login'})
