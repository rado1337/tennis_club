from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourtViewSet, ReservationViewSet, reservation_view, register_view

# Tworzymy router dla widoków API
router = DefaultRouter()
router.register(r'courts', CourtViewSet)
router.register(r'reservations', ReservationViewSet)

# Definiujemy URL-e
urlpatterns = [
    path('', reservation_view, name='reservations'),  # Strona rezerwacji
    path('register/', register_view, name='register'),  # Strona rejestracji
    path('api/', include(router.urls)),  # Ścieżki API
]
