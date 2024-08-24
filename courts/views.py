from django.shortcuts import render, redirect
from courts.forms import CustomUserCreationForm, ProfileForm
from rest_framework import viewsets
from .models import Court, Reservation
from .serializers import CourtSerializer, ReservationSerializer
from rest_framework.permissions import IsAuthenticated
from datetime import time

def reservation_view(request):
    hours = [time(hour, 0).strftime('%H:%M') for hour in range(10, 19)]
    courts = list(range(1, 7))  # Numery kortów od 1 do 6
    context = {
        'hours': hours,
        'courts': courts,
    }
    return render(request, 'courts/reservation.html', context)


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
    return render(request, 'courts/register.html', {'user_form': user_form, 'profile_form': profile_form})

# Widok API dla modelu Court
class CourtViewSet(viewsets.ModelViewSet):
    queryset = Court.objects.all()
    serializer_class = CourtSerializer
    permission_classes = [IsAuthenticated]

# Widok API dla modelu Reservation
class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]
