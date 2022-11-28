from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .forms import customForm,userupdate,profileupdate
from blog.models import postblog

# Create your views here.
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form=customForm(request.POST)
        if form.is_valid():   
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}!')
            return redirect('blog-home')
    else:
        form=customForm()
    return render(request,'users/register.html',{'form':form})

def userlogin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username)
        print(password)
        user = authenticate(request,username=username, password=password)
        if user is not None:
            return redirect('blog-home')
    return render(request,'users/login.html')

@login_required
def profile(request):
    if request.method == 'POST':
        u_form=userupdate(request.POST,instance=request.user)
        p_form=profileupdate(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,'Your account has been updated')
            return redirect('user-profile')
    else:
        u_form=userupdate(instance=request.user)
        p_form=profileupdate(instance=request.user.profile)

    data={
        'u_form':u_form,
        'p_form':p_form,
        'posts':postblog.objects.all(),
    }
    return render(request,'users/profile.html',context=data)
