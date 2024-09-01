from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Profile
from django.forms import ModelForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        labels = {
            "username": "Nazwa użytkownika",
            "email": "Adres email",
        }
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].label = "Hasło"
        self.fields['password2'].label = "Potwierdź hasło"


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = [
            "profile_image",
        ]
        labels = {
            "profile_image": "Zdjęcie użytkownika",
        }

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for __name__, field in self.fields.items():
            field.widget.attrs.update({"class": "input"})
