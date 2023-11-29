import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _


class TimeStampModel(models.Model):
    class Meta:
        abstract = True

    created_on = models.DateTimeField(
        auto_now_add=True,
    )

    updated_on = models.DateTimeField(
        auto_now=True,
    )


class MonthChoices(models.TextChoices):
    JANUARY = 'January'
    FEBRUARY = 'February'
    MARCH = 'March'
    APRIL = 'April'
    MAY = 'May'
    JUNE = 'June'
    JULY = 'July'
    AUGUST = 'August'
    SEPTEMBER = 'September'
    OCTOBER = 'October'
    NOVEMBER = 'November'
    DECEMBER = 'December'


class YearChoices(models.TextChoices):
    @staticmethod
    def next_five_years():
        today = datetime.date.today()
        year = today.year
        period = 5
        years = [year - 1 + i for i in range(period)]

        return years

    YEAR_0 = next_five_years()[0], _(str(next_five_years()[0]))
    YEAR_1 = next_five_years()[1], _(str(next_five_years()[1]))
    YEAR_2 = next_five_years()[2], _(str(next_five_years()[2]))
    YEAR_3 = next_five_years()[3], _(str(next_five_years()[3]))
    YEAR_4 = next_five_years()[4], _(str(next_five_years()[4]))


class MonthlyBill(models.Model):
    class Meta:
        abstract = True

    month = models.CharField(
        max_length=64,
        choices=MonthChoices.choices,
    )

    year = models.CharField(
        max_length=10,
        choices=YearChoices.choices,
    )

    electricity_common = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    electricity_lift = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    internet = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    maintenance_lift = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    fee_cleaner = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    fee_manager_and_cashier = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    repairs = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    others = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
    )
