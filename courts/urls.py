from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourtViewSet, ReservationViewSet, reservation_view, index, register

# Tworzymy router dla widoków API
router = DefaultRouter()
router.register(r'courts', CourtViewSet)
router.register(r'reservations', ReservationViewSet)

# Definiujemy URL-e
urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('reservations/', reservation_view, name='reservation'),
    path('api/', include(router.urls)),  # Dodajemy ścieżki API
]
