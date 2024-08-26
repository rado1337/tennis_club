from django.shortcuts import render
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

class CourtViewSet(viewsets.ModelViewSet):
    queryset = Court.objects.all()
    serializer_class = CourtSerializer
    permission_classes = [IsAuthenticated]

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]
