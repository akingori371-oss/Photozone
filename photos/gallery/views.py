from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login , logout 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, "gallery/home.html")

def register(request):
    if request.method == "POST":
      form = UserCreationForm(request.POST)

      if form.is_valid():
         form.save()
         return redirect("login")

      else:
         form = UserCreationForm()
      return render(request , "gallery/register.html" , {"form" : form})  

def login(request):
   if request.method == "POST":
      username = request.POST("username")    
      password = request.POST("password") 

      user = authenticate(
         request,
         username=username,
         password=password
        
      )
      if user is not None:
         login(request , user)
         return render("gallery_home")
      return render(
         request,
         "gallery/login.html",
         {"error" : "invalid username or password."}
      )   
   return render(request, login.html)

def logout(request):
   if request.method == "POST":
      logout(request)
      return render("gallery_home")

@login_required
def gallery_home(request):
   return render (request , "gallery/gallery_home.html")   
   
    
