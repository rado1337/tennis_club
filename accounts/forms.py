from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Profile
from django.forms import ModelForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_image','tags',]

        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }
    
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for __name__, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})