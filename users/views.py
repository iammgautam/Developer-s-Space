from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CustomUserCreationForm

from .models import Profile
from django.contrib.auth.models import User
# Create your views here.

def loginUser(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('profile')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "Username doesn't Exist")

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, "Username or Password is Incorrect")

    # context = {
    #     'page':page,
    # }
    return render(request, 'users/login_register.html')

def logoutUser(request):
    logout(request)
    messages.error(request, "User was loged Out!!")
    return redirect('login')

def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'Account Created Successfully!!')

            login(request, user)
            return redirect('profile')
        else:
            messages.success(request, "An Error has Occurred During Registration.")

    context = {
        'page':page,
        'form':form,
    }
    return render(request, 'users/login_register.html', context)

def profile(request):
    profiles = Profile.objects.all()
    context = {
        'profiles':profiles,
    }
    return render(request, 'users/profile.html', context)

def userProfile(request, pk):
    profile = Profile.objects.get(id = pk)
    topskills = profile.skill_set.exclude(description__exact = '')
    otherskills = profile.skill_set.filter(description='')
    
    context = {
        'profile':profile,
        'topskill':topskills,
        'otherskill': otherskills,
    }
    return render(request, 'users/user-profile.html', context)