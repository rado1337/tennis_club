from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourtViewSet, ReservationViewSet, reservation_view


router = DefaultRouter()
router.register(r'courts', CourtViewSet)
router.register(r'reservations', ReservationViewSet)


urlpatterns = [
    path('', reservation_view, name='reservations'),  
    path('api/', include(router.urls)),  
]
