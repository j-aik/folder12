from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.shortcuts import render
from . models import Place



def demo(request):
  obj = Place.objects.all()
  return render(request,"template.html",{'result':obj })

def register(request):

  if request.method == 'POST':
    username = request.POST['username']
    First_name = request.POST[' First_name ']
    last_name = request.POST[' last_name']
    password = request.POST['password']
    email = request.POST['email']
    cpassword = request.POST['password1']
    if password == cpassword:

       if User.objects.filter(username=username).exists():
           messages.info(request, "username taken")
           return redirect('register')

       elif User.objects.filter(email=email).exists():
            messages.info(request, "email taken")
            return redirect('register')

       else:
            user = User.objects.create_user(username= username, password= password, First_name= First_name, last_name=last_name,email=email)
            user.save();


    else:
       messages.info(request, "password is not correct")
       return redirect ('register')

    return redirect('/')

  return render(request, "register.html")



