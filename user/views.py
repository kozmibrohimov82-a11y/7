from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login,logout
from .forms import *

def register_view(request):
    if request.method=='POST':
        form=RegisterForm(data=request.POST)
        if form.is_valid():
            user=form.save()
            return redirect('index')
    else:
        form=RegisterForm()

    contex={
        'form':form,
    }
    return render(request,'register.html',contex)

def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('home')

    form=AuthenticationForm()
    context={
        'form':form
    }
    return render(request,'login.html',context)

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def profile(request):
    return render(request,'profile.html')
