from django import forms

from applications.order.models import Order


class CreateOrderForm(forms.ModelForm ):
    class Meta:
        model = Order
        fields = '__all__'