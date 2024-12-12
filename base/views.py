from django.shortcuts import render
from django.views import View
from .forms import Registration
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate

# Home page view 
def home_page(request):
    return render(request,"home.html")

# Signup View 
class SignUp(View):
    def get(self,request):
        if not request.user.is_authenticated:
            form = Registration(auto_id=True)
            return render(request,"signup.html",{"form":form})
        else:
            return HttpResponseRedirect("/")
    
    def post(self,request):
        if not request.user.is_authenticated:
            form = Registration(auto_id=True,data=request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("/login")
            return render(request,"signup.html",{"form":form})
        else:
            return HttpResponseRedirect("/")

# Login View 
class Login(View):
    def get(self,request):
        if not request.user.is_authenticated:
            form = AuthenticationForm()
            return render(request,"login.html",{"form":form})
        else:
            return HttpResponseRedirect("/")
    
    def post(self,request):
        if not request.user.is_authenticated:
            form = AuthenticationForm(request,data=request.POST)
            if form.is_valid():
                username,password = form.cleaned_data.values()
                user = authenticate(request,username=username,password=password)
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect("/")
            return render(request,"login.html",{"form":form})
        else:
            return HttpResponseRedirect("/")
        
def logout_page(request):
    logout(request)
    return HttpResponseRedirect("/")