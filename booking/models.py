from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import CharField, PositiveIntegerField, ForeignKey, CASCADE
from django.core.validators import MinValueValidator
from django.contrib.postgres.constraints import ExclusionConstraint
from django.contrib.postgres.fields import (
    DateRangeField,
    RangeOperators,
)


class Room(models.Model):
    name = CharField(max_length=50)
    price = PositiveIntegerField()
    size = PositiveIntegerField(validators=[MinValueValidator(1)])

    def __str__(self) -> str:
        return f'{self.name}'


class Reservation(models.Model):
    room = ForeignKey("Room", on_delete=CASCADE)
    guest = ForeignKey(get_user_model(), on_delete=CASCADE)
    timespan = DateRangeField()

    class Meta:
        constraints = [
            ExclusionConstraint(
                name='exclude_overlapping_reservations',
                expressions=[
                    ('timespan', RangeOperators.OVERLAPS),
                    ('room', RangeOperators.EQUAL),
                ],
            ),
        ]