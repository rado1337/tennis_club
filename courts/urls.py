from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CourtViewSet,
    ReservationViewSet,
    reservation_view,
    CreateReservationView,
    reservation_grid,
    reserve,
)


router = DefaultRouter()
router.register(r"courts", CourtViewSet)
router.register(r"reservations", ReservationViewSet)


urlpatterns = [
    path("", reservation_view, name="reservations"),
    path("api/", include(router.urls)),
    path(
        "api/create-reservation/",
        CreateReservationView.as_view(),
        name="create-reservation",
    ),
    path("reservation_grid/", reservation_grid, name="reservation_grid"),
    path("reserve/", reserve, name="reserve"),
]
