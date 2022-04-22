from django.urls import include, path

from applications.order.views import create_order

urlpatterns = [
    path('create/', create_order, name='create-order')



]
