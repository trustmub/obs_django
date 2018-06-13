from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class CustomerDashboard(TemplateView):
    template_name = 'customer_dashboard.html'


class AddCustomer(TemplateView):
    template_name = 'add_customer.html'
