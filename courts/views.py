from django.shortcuts import render
from rest_framework import viewsets
from .models import Court, Reservation
from .serializers import CourtSerializer, ReservationSerializer
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated
from datetime import time
from rest_framework.views import APIView
from rest_framework.response import Response
from copy import deepcopy
from datetime import datetime
from datetime import timedelta
from django.http import HttpResponse
from django.shortcuts import redirect


def reservation_view(request):
    hours = [time(hour, 0).strftime("%H:%M") for hour in range(10, 19)]
    courts = Court.objects.all().values_list("number", flat=True)
    date = datetime.now().date()
    reservations = Reservation.objects.filter(start_time__icontains=date).values_list(
        "start_time", flat=True
    )
    time_list = []
    for time_data in reservations:
        time_list.append(datetime.strftime(time_data, "%H:%M"))
    print(time_list)
    # courts = list(range(1, 7))  # Numery kortów od 1 do 6
    context = {"hours": hours, "courts": courts, "time_list": time_list}
    return render(request, "courts/reservation.html", context)


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
            court_id, hour = reservation.split("-")
            court_for_create = Court.objects.get(number=court_id)
            datetime_str: str = f"2024-08-27 {hour}"
            datetime_object = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M")
            end_hour = datetime_object + timedelta(hours=1)
            Reservation.objects.create(
                court=court_for_create,
                user=request.user,
                start_time=datetime_object,
                end_time=end_hour,
                type="regular",
            )
        return Response(request.data)


def reservation_grid(request):
    selected_date = request.GET.get("date")
    if not selected_date:
        selected_date = datetime.today().strftime("%Y-%m-%d")

    selected_date = datetime.strptime(selected_date, "%Y-%m-%d")

    courts = Court.objects.all()
    reservations = Reservation.objects.filter(start_time__date=selected_date)

    time_slots = [time(hour, 0) for hour in range(10, 19)]
    context = {
        "courts": courts,
        "reservations": reservations,
        "types": [
            ("regular", "Zwykła"),
            ("league", "Liga Format"),
            ("school", "Trening"),
            ("membership", "ClubCard"),
        ],
        "time_slots": time_slots,
        "selected_date": selected_date.strftime("%Y-%m-%d"),
    }

    return render(request, "reservation_grid.html", context)


@login_required
def reserve(request):
    if request.method == "POST":
        court_id = request.POST.get("court_id")
        start_time = request.POST.get("start_time")
        reservation_type = request.POST.get("reservation_type")
        normalized_date_str = start_time.replace("a.m.", "AM").replace("p.m.", "PM")
        # Parse the date string into a datetime object
        date_obj = datetime.strptime(normalized_date_str, "%Y-%m-%d %H:%M:%S")

        # Format the datetime object into the desired format
        end_time = date_obj + timedelta(hours=1)

        court = Court.objects.get(id=court_id)

        # Ensure no overlapping reservations
        if Reservation.objects.filter(
            court=court, start_time__lt=end_time, end_time__gt=date_obj
        ).exists():
            return HttpResponse("This time slot is already reserved.", status=400)

        reservation = Reservation.objects.create(
            court=court,
            user=request.user,
            start_time=date_obj,
            end_time=end_time,
            type=reservation_type,
        )

        return redirect("reservation_grid")
