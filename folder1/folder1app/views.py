from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.shortcuts import render
from . models import Place



def demo(request):
  obj = Place.objects.all()
  return render(request,"index.html",{'result':obj})


# Create your views here.


