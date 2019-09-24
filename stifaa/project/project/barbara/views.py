from django.shortcuts import render
from django.http import HttpResponse

def barbara(request):
    return render(request ,'barbara.html')
