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
        fields = ['profile_image', 'tags']

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['court', 'start_time', 'end_time', 'type']
