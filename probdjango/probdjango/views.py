from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    a=15+32584
    return render(request,"about.html",{'gretting':a})



def home(request):
    return HttpResponse("это домашняя страница")
