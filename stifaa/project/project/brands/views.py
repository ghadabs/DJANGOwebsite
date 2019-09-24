from django.shortcuts import render
from django.http import HttpResponse

def brand(request):
    return render(request ,'saveurs.html')