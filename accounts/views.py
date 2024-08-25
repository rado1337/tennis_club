from django.shortcuts import render, redirect
from courts.forms import CustomUserCreationForm, ProfileForm

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
