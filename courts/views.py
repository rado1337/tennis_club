from django.shortcuts import render
from rest_framework import viewsets
from .models import Court, Reservation
from .serializers import CourtSerializer, ReservationSerializer
from rest_framework.permissions import IsAuthenticated
from datetime import time
from rest_framework.views import APIView
from rest_framework.response import Response
from copy import deepcopy
from datetime import datetime
from datetime import timedelta

def reservation_view(request):
    hours = [time(hour, 0).strftime('%H:%M') for hour in range(10, 19)]
    courts = Court.objects.all().values_list("number", flat=True)
    reservations = Reservation.objects.all().values_list("start_time", flat=True)
    time_list = []
    for time_data in reservations:
        time_list.append(datetime.strftime(time_data, '%H:%M'))
    print(time_list)
    # courts = list(range(1, 7))  # Numery kortów od 1 do 6
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


class CreateReservationView(APIView):

    def post(self, request, *args, **kwargs):
        data: list[str] = deepcopy(request.data)
        for reservation in data:
            court_id, hour = reservation.split('-')
            court_for_create = Court.objects.get(number=court_id)
            datetime_str: str = f'2024-08-27 {hour}'
            datetime_object = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M')
            end_hour = datetime_object + timedelta(hours=1)
            Reservation.objects.create(court=court_for_create, user=request.user, start_time=datetime_object, end_time=end_hour, type='regular')
        return Response(request.data)
