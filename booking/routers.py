from booking.views import ReservationViewSet, RoomViewSet
from core.router import router

router.register(r'rooms', RoomViewSet, basename='rooms')
router.register(r'reservs', ReservationViewSet, basename='reservs')
