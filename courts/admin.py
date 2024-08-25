from django.contrib import admin

# Register your models here.
from .models import Court, Reservation

admin.site.register(Reservation)
admin.site.register(Court)

