from django.contrib import admin

from booking.models import Reservation, Room


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['room', 'guest', 'timespan']
    search_fields = ['room', 'guest']

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'size']
    list_filter = ['price', 'size']
    search_fields = ['name']