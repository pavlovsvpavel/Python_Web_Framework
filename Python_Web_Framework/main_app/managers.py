from django.db import models
from django.db.models import Q, F, Sum


class CustomerMonthlyBillManager(models.Manager):
    def calculate_total_amount(self, customer_id, month, year):
        """
        :params: collected from user input
        """
        query = Q(customer=customer_id) & Q(month=month) & Q(year=year)
        customer = self.filter(query)

        customer.update(
            total_amount=
            F('electricity_common') +
            F('electricity_lift') +
            F('internet') +
            F('maintenance_lift') +
            F('fee_cleaner') +
            F('fee_manager_and_cashier') +
            F('repairs') +
            F('others')
        )


class CustomerClientManager(models.Manager):
    def total_people(self, customer_id):
        """
        :params: collected from user input
        """

        query = Q(customer__id=customer_id)

        people = (
            self
            .select_related('customer_clients')
            .filter(query)
            .aggregate(total_people=Sum('number_of_people'))
        )

        return people['total_people']

    def total_people_using_lift(self, customer_id):
        """
        :params: collected from user input
        """

        query = Q(customer__id=customer_id) & Q(is_using_lift=True)

        people = (
            self
            .select_related('customer_clients')
            .filter(query)
            .aggregate(total_people=Sum('number_of_people'))
        )

        return people['total_people']
