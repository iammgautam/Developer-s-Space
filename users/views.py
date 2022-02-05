from pydoc import describe
from django.shortcuts import render
from .models import Profile

# Create your views here.

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