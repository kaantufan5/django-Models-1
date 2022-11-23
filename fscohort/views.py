from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("Welcome back-end")

def starter(request):
    return HttpResponse("Congratulations!")
