from django.urls import path
from .views import AuthentView
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('',AuthentView.as_view()),

]