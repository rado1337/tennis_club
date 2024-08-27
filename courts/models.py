from django.utils import timezone
from django.db import models
from accounts.models import User


class Court(models.Model):
    number = models.IntegerField(unique=True)  
    type = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)  
    is_available = models.BooleanField(default=True) 

    def __str__(self):
        return f"Court {self.number}: {self.type}"


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
    type = models.CharField(max_length=50, choices=RESERVATION_TYPE_CHOICES)  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.court} - {self.start_time} to {self.end_time}"

    class Meta:
        unique_together = ('court', 'start_time', 'end_time')  


