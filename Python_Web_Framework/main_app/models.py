from django.db import models

from Python_Web_Framework.main_app.mixins import TimeStampModel,  MonthlyBill
from Python_Web_Framework.main_app.validators import validate_char_field, validate_phone_number


class User(TimeStampModel):
    first_name = models.CharField(
        max_length=30,
        validators=[
            validate_char_field
        ],
    )

    last_name = models.CharField(
        max_length=30,
        validators=[
            validate_char_field
        ],
    )

    password = models.CharField(
        max_length=256,
    )

    email = models.EmailField()

    phone_number = models.CharField(
        max_length=10,
        validators=[
            validate_phone_number,
        ]
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Customer(TimeStampModel):
    town = models.CharField(
        max_length=20,
        validators=[
            validate_char_field,
        ]
    )

    address = models.CharField(
        max_length=100,
    )

    building_number = models.PositiveIntegerField(
        blank=True,
        null=True,
    )

    entrance = models.CharField(
        max_length=1,
    )

    user = models.ForeignKey(
        to='User',
        null=True,
        on_delete=models.CASCADE,
        related_name='customers'
    )

    def __str__(self):
        return (f"{self.town}, {self.address}, "
                f"{self.building_number}, {self.entrance}")


class CustomerClient(TimeStampModel):
    class Meta:
        unique_together = ['apartment', 'customer']
        ordering = ['customer', 'apartment']

    family_name = models.CharField(
        max_length=30,
        validators=[
            validate_char_field,
        ]
    )

    floor = models.PositiveIntegerField()

    apartment = models.PositiveIntegerField()

    number_of_people = models.PositiveIntegerField()

    is_using_lift = models.BooleanField(
        default=True,
    )

    is_occupied = models.BooleanField(
        default=True,
    )

    fixed_fee = models.BooleanField(
        default=False,
    )

    customer = models.ForeignKey(
        to='Customer',
        on_delete=models.CASCADE,
        related_name='customer_clients'
    )

    def __str__(self):
        return self.family_name


class CustomerMonthlyBill(MonthlyBill):
    customer = models.ForeignKey(
        to='Customer',
        on_delete=models.CASCADE,
        related_name='customer_monthly_bills'
    )


class CustomerClientMonthlyBill(MonthlyBill):
    customer_client = models.ForeignKey(
        to='CustomerClient',
        on_delete=models.CASCADE,
        related_name='customer_client_monthly_bills'
    )
