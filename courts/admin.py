from django.contrib import admin
from .models import Court, Reservation

admin.site.register(Reservation)
admin.site.register(Court)

