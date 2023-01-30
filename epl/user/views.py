from django.shortcuts import render,redirect
from django.contrib.auth import login as auth_login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Profile
from .forms import CustomUserForm ,CustomLoginForm, ProfileForm, FavTeamForm
from django.contrib import messages
from teams.models import Team
from rest_framework.authtoken.models import Token
# Create your views here.

def login(request):
    page = 'login'
    form = CustomLoginForm()
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist!')

        user = authenticate(request, username=username, password=password) # make sure user username and password is corect

        if user is not None:
            auth_login(request, user)
            messages.success(request, "Logged in Successfully")
            return redirect('home')

        elif username != request.POST['username'] or password != request.POST['password'] :
            messages.error(request,'Username or Password incorrect')

    context = {'page': page, 'form': form }
    return render(request, 'login_register.html',context)

@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    messages.success(request, 'User logged out!')
    return redirect('home')


def register(request):
    page = 'register'
    form = CustomUserForm()

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()

            user.save()
            messages.success(request, 'User created')

            auth_login(request, user)
            return redirect('edit-profile')
        else:
            messages.error(request, 'Registration Error')
    context = {'page': page, 'form':form}
    return render(request,'login_register.html',context)

@login_required(login_url="login")
def editProfile(request):
    # signals.py has signals that saves a profile when user is created
    profile = request.user.profile
    form = ProfileForm(instance=profile)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form, 'profile':profile}
    return render(request, 'edit-profile.html',context)

def addTeam(request):
    profile = request.user.profile
    form = FavTeamForm()

    if request.method == 'POST':
        team=request.POST.get('team')
        print(team)
        profile_favteam = Profile.objects.update_or_create(user=profile, fav_team=team)
        profile_favteam.save()
        return render(request,"teams/home.html")

        # form = FavTeamForm(request.POST)
        # if form.is_valid():
        #     team = form.save(commit=False)
        #     team.save()
        #     messages.success(request,"Message sent")
        #     return redirect('home')






