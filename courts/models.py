from django.utils import timezone
from django.db import models
from accounts.models import User


# Model dla kortu tenisowego
class Court(models.Model):
    number = models.IntegerField(unique=True)  # Numer kortu musi być unikalny
    type = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)  # Dodano opis kortu
    is_available = models.BooleanField(default=True)  # Czy kort jest dostępny

    def __str__(self):
        return f"Court {self.number}: {self.type}"

# Model rezerwacji
class Reservation(models.Model):
    RESERVATION_TYPE_CHOICES = [
        ('regular', 'Zwykła'),
        ('league', 'Liga Format'),
        ('school', 'Trening'),
        ('membership', 'ClubCard'),
    ]

    court = models.ForeignKey(Court, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    type = models.CharField(max_length=50, choices=RESERVATION_TYPE_CHOICES)  # Typ rezerwacji jako wybór z listy
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} - {self.court} - {self.start_time} to {self.end_time}"

    class Meta:
        unique_together = ('court', 'start_time', 'end_time')  # Unikalność rezerwacji na kort i czas


