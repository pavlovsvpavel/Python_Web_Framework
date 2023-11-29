from django.contrib import admin

from Python_Web_Framework.main_app.models import User, Customer, CustomerClient, CustomerMonthlyBill


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone_number']
    list_filter = ['customers']


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['town', 'address', 'building_number', 'entrance']


@admin.register(CustomerClient)
class CustomerClient(admin.ModelAdmin):
    list_display = [
        'family_name', 'floor', 'apartment',
        'number_of_people', 'is_occupied',
        'is_using_lift', 'fixed_fee', 'customer'
    ]
    list_filter = ['customer']


@admin.register(CustomerMonthlyBill)
class CustomerMonthlyBillAdmin(admin.ModelAdmin):
    list_display = [
        'month', 'year', 'electricity_common',
        'electricity_lift', 'internet', 'maintenance_lift',
        'fee_cleaner', 'fee_manager_and_cashier', 'repairs',
        'others', 'total_amount'
    ]

