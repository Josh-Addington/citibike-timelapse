from django.contrib import admin
from map.models import Station, TripStart, TripEnd

# Register your models here.
admin.site.register(Station)
admin.site.register(TripStart)
admin.site.register(TripEnd)
