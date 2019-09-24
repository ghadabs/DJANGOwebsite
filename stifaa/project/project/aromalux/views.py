from django.shortcuts import render
from django.http import HttpResponse

def aromalux(request):
    return render(request ,'aromalux.html')