from django.urls import path, include
from rest_framework.routers import DefaultRouter


from applications.product.views import *

router = DefaultRouter()
router.register('', ProductViewSet)


urlpatterns = [

    path('category/', CategoryListCreateView.as_view()),
    path('category/<str:slug>', CategoryDeleteUpdateRetriveView.as_view()),
    path('', include(router.urls)),

]