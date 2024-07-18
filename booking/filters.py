import django_filters
from django.db.models import Q
from booking.models import Room, Reservation


class RoomFilterSet(django_filters.FilterSet):
        
        daterange = django_filters.DateFromToRangeFilter(method='filter_daterange', label='Date range')

        def filter_daterange(self, queryset, name, value):
            start_date = value.start.date()
            end_date = value.stop.date()
            reservation_set = Reservation.objects.filter(Q(timespan__startswith__gt=end_date) | Q(timespan__endswith__lt=start_date))
            queryset = queryset.filter(reservation__in=reservation_set).distinct()
            return queryset

        class Meta:
            model = Room
            fields = ['size', 'price']