from django.http import HttpResponse
from django.shortcuts import render
import json



def AboutMe(request):
    return render(request, 'home/AboutMe.html')