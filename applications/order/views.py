from django.shortcuts import render

from applications.order.forms import CreateOrderForm
from applications.order.models import Order


def create_order(request):
    order_form = CreateOrderForm(request.POST)
    if order_form.is_valid():
        # order = Order.objects.create(order_form.cleaned_data)
        order_form.save()
        return render(request, 'order/')
    order_form = CreateOrderForm
    return render(request, 'order/')