from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse('<center><h1 style="background-color:powderblue;">Welcome to ApiTodo<h1><center>')
