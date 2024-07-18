import django_filters
from booking.models import Room, Reservation


class RoomFilterSet(django_filters.FilterSet):
        
        daterange = django_filters.DateFromToRangeFilter(method='filter_daterange', label='Date range')

        def filter_daterange(self, queryset, name, value):
            start_date = value.start.date()
            end_date = value.stop.date()
            reservation_set = Reservation.objects.all().values()
            filter = []
            for daterange in reservation_set:
                start = daterange['timespan'].lower
                end = daterange['timespan'].upper
                if start_date > end or end_date < start:
                    filter.append(daterange['room_id'])
                result = queryset.filter(id__in=filter)
            return result

        class Meta:
            model = Room
            fields = ['size', 'price']