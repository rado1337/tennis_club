from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Profile, Reservation

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'location', 'profile_image', 'social_twitter', 'social_facebook', 'tags']

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['court', 'start_time', 'end_time', 'type']
