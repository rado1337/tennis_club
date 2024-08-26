from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True, default="Oława")
    card_id = models.CharField(max_length=255, unique=True)
    bio = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to='profiles/', blank=True, default='profiles/tenis_17.png')
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tag', blank=True)

    @property
    def imageURL(self):
        try:
            url = self.profile_image.url
        except:
            url = 'media/profiles/tenis_17.png'
        return url

def __str__(self):
    return str(self.user.username)


class Tag(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Trainer(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=255)

    def __str__(self):
        return f"Trainer: {self.profile.user.username}, Specialization: {self.specialization}"