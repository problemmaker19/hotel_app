from rest_framework import serializers
from booking.models import Reservation, Room


class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
    room = RoomSerializer()
    guest = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )

    class Meta:
        model = Reservation
        fields = ['room', 'timespan', 'guest']

