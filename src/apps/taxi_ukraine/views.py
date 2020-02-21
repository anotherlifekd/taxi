from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Drivers
from .forms import OrderForm, GetEditOrderStatusForm, PostEditOrderStatusForm, check_user_group
from .models import User, Order

from apps.order_status_choices import IN_PROCESSING, COMPLETED


def taxi(request):
    return render(request, 'base.html')


def order(request):
    if request.method == 'GET':
        form = OrderForm
    elif request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            try:
                free_driver = Drivers.objects.filter(is_free=True).first()
                if free_driver:
                    free_driver.is_free = False
                    brand = free_driver.license_plate_number.get_car_brand_display()
                    free_driver.save()
                else:
                    return HttpResponse('Sorry! All drivers are busy')
            except:
                return Http404('Some error')
            form.instance.taxi_driver = free_driver.id
            form.instance.status = IN_PROCESSING
            form.save()
            return HttpResponse(f'Number of your order: {form.instance.id}  / Car: {brand}')

    return render(request, 'taxi/create_order.html', {'form': form})


@login_required(login_url='/accounts/login/')
def user_profile(request):
    user = User.objects.get(username=request.user.username)
    user_group = str(request.user.groups.all())

    orders = Order.objects.filter(taxi_driver=user.id) if 'Drivers' in user_group else Order.objects.all()
    paginator = Paginator(orders, 10)
    page = request.GET.get('page')
    orders = paginator.get_page(page)
    context = {
        'user': user,
        'orders': orders
    }
    return render(request, 'registration/user_profile.html', context=context)


@login_required(login_url='/accounts/login/')
def edit_order_status(request, id):
    order = Order.objects.get(id=id)

    if request.method == 'GET':
        user_groups = check_user_group(request.user.groups.all())
        form = form = GetEditOrderStatusForm(instance=order, user_groups=user_groups)
    elif request.method == "POST":
        form = form = PostEditOrderStatusForm(request.POST, instance=order)
        if form.is_valid():
            if getattr(form.instance, 'status', '') == COMPLETED:
                driver = Drivers.objects.get(id=request.user.id)
                driver.is_free = True
                driver.save()
            form.save()
    context = {
        'form': form,
        'order': order
    }
    return render(request, 'taxi/edit_order_status.html', context=context)
