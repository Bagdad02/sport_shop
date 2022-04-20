from rest_framework.generics import ListCreateAPIView

from applications.order.models import Order
from applications.order.serializers import OrderSerializers


class OrderListCreateView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers
