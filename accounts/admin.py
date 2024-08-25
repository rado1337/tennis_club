from django.contrib import admin

# Register your models here.
from .models import Profile, Tag, Trainer

admin.site.register(Profile)
admin.site.register(Tag)
admin.site.register(Trainer)