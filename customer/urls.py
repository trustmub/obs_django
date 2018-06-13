from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.CustomerDashboard.as_view()),
    path('new_customer/', views.AddCustomer.as_view())
]
