import re

from django.db.models.query import QuerySet
from django.forms import ModelForm
from .models import Order

from apps.order_status_choices import DISPATCH_STATUS_ORDER, DRIVER_STATUS_ORDER


class OrderForm(ModelForm):

    def clean_client_name(self):
        cleaned_data = self.clean()
        client_name = cleaned_data.get('client_name', '')
        if not has_cyrillic(client_name):
            self.add_error('client_name', 'Should be cyrillic letters')
        return client_name

    def clean_phone(self):
        cleaned_data = self.clean()
        phone_number = cleaned_data.get('phone', '')
        if not is_ukrainian_phone_number_phormat(phone_number.raw_input):
            self.add_error('phone', 'Should be Ukrainian format: +380(ХХ)ХХХ-ХХ-ХX')
        return phone_number

    class Meta:
        model = Order
        fields = ['client_name', 'phone', 'order_address', 'distination_address', 'desired_time']


class GetEditOrderStatusForm(ModelForm):

    def __init__(self, *args, user_groups=list, **kwargs):
        super(GetEditOrderStatusForm, self).__init__(*args, **kwargs)
        if 'Dispatch' in user_groups:
            self.fields['status'].choices = DISPATCH_STATUS_ORDER
        if 'Drivers' in user_groups:
            self.fields['status'].choices = DRIVER_STATUS_ORDER

    class Meta:
        model = Order
        fields = ['status']


class PostEditOrderStatusForm(ModelForm):

    class Meta:
        model = Order
        fields = ['status']


def check_user_group(groups: QuerySet) -> list:
    return [i.name for i in groups]


def has_cyrillic(text: str) -> bool:
    return bool(re.search('[\u0400-\u04FF]', text))


def is_ukrainian_phone_number_phormat(number: str) -> bool:
    return bool(re.search('^(?:\+380)[(][0-9]{2}[)][0-9]{3}[-][0-9]{2}[-][0-9]{2}$', number))
