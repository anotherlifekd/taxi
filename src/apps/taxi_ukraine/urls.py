from django.urls import path
from .views import order, taxi, user_profile, edit_order_status

app_name = 'taxi_ukraine'
urlpatterns = [
    path('', taxi),
    path('order/', order),
    path('order-status/<id>', edit_order_status),
    path('profile/', user_profile)
]
