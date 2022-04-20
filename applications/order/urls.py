from django.urls import include, path

from applications.order.views import OrderListCreateView

urlpatterns = [

    path('order/', OrderListCreateView.as_view()),

]
