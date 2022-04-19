from django.urls import path

from applications.account.views import RegisterApiView, ActivationView, LoginApiView, LogoutView

urlpatterns = [
    path('register/', RegisterApiView.as_view()),
    path('activate/<uuid:activation_code>/', ActivationView.as_view()),
    path('login/', LoginApiView.as_view()),
    path('logout/', LogoutView.as_view()),

]


