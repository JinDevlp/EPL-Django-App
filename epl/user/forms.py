from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from teams.models import Team

class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name','email','username','profile_image']

class CustomLoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class FavTeamForm(ModelForm):
    class Meta:
        model = Team
        fields = ('shortname',)

