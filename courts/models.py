from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.db import models

# Użytkownik z dodatkowymi polami
class User(AbstractUser):
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='courts_user_set',  
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='courts_user_set',  
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

# Profil użytkownika
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance_of_hours = models.IntegerField(default=0)
    card_id = models.CharField(max_length=255, unique=True)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=255, blank=True)
    profile_image = models.ImageField(upload_to='profile_images', blank=True)
    social_twitter = models.CharField(max_length=255, blank=True)
    social_facebook = models.CharField(max_length=255, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tag', blank=True)

# Tag dla profilu użytkownika
class Tag(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

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

# Model trenera
class Trainer(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=255)

    def __str__(self):
        return f"Trainer: {self.profile.user.username}, Specialization: {self.specialization}"
