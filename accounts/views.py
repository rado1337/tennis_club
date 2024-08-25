from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserCreationForm, ProfileForm
from .models import Profile


def register_view(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('home')
    else:
        user_form = CustomUserCreationForm()
        profile_form = ProfileForm()
    return render(request, 'accounts/register.html', {'user_form': user_form, 'profile_form': profile_form})

def profiles_view(request):
    profiles = Profile.objects.all()
    return render(request, 'accounts/profiles.html', {'profiles': profiles})

def profile_detail_view(request, id):
    profile = get_object_or_404(Profile, id=id)
    return render(request, 'accounts/profile_detail.html', {'profile': profile})