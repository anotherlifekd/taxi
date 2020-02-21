from django.contrib import admin
from .models import Cars, Drivers, Dispatch, Order


@admin.register(Cars)
class CarsAdmin(admin.ModelAdmin):
    list_display = ['license_plate_number', 'color', 'car_brand']


@admin.register(Drivers)
class DriversAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'license_plate_number', 'is_free']


@admin.register(Dispatch)
class DispatchAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'office', 'salary']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'phone', 'order_address', 'distination_address', 'desired_time', 'status', 'taxi_driver']
