from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth import logout


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Welcome {username}, Your Account is created!")
            return redirect('users:login')
    else:
        form = RegisterForm()
    return render(request,'users/register.html',{'form':form})



def LogoutView(request):
    logout(request)
    return redirect('/')
    # return render(request,'users/logout.html')