from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from apps.car_brand_choices import CAR_BRAND_CHOICES as cb_choices
from apps.order_status_choices import ORDER_STATUS_CHOICES as os_choices

from phonenumber_field.modelfields import PhoneNumberField


class Cars(models.Model):
    license_plate_number = models.CharField(max_length=12, primary_key=True, unique=True)
    color = models.CharField(max_length=50)  # 50 - info from internet
    car_brand = models.SmallIntegerField(choices=cb_choices)

    def __str__(self):
        return self.license_plate_number

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'


class Drivers(User):
    license_plate_number = models.ForeignKey(
        Cars, to_field="license_plate_number", db_column="taxi_ukraine_cars", on_delete=models.PROTECT
    )
    is_free = models.BooleanField(default=True)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Driver'
        verbose_name_plural = 'Drivers'


class Dispatch(User):
    office = models.SmallIntegerField()
    salary = models.DecimalField(max_digits=8, decimal_places=2)  # 999,999.99

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Dispatch'
        verbose_name_plural = 'Dispatches'


class Order(models.Model):
    client_name = models.CharField(max_length=30)
    phone = PhoneNumberField()
    order_address = models.CharField(max_length=120)
    distination_address = models.CharField(max_length=120)
    desired_time = models.DateTimeField(default=datetime.now, blank=True)
    status = models.SmallIntegerField(choices=os_choices, default=1)
    taxi_driver = models.IntegerField(blank=True)
