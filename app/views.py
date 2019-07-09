from django.shortcuts import render
from django import views


def index(request):

    return render(request,'index.html')

def register(request):
    return render(request,'register.html')

def password(request):
    return render(request,'password.html')

def change_password(request):
    return  render(request,'change_password.html')