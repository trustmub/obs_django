from django.utils import timezone
from django.db import models
from customer.models import Customer

from django.contrib.auth.models import User


# Create your models here.
class AccountType(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=5)
    create_by = models.ForeignKey(User, related_name='created_by', on_delete=models.SET_NULL, null=True)
    create_date = models.DateTimeField(timezone.now)
    authorised_by = models.ForeignKey(User, related_name='authorised_by', on_delete=models.SET_NULL, null=True)
    authorise_date = models.DateTimeField()
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Account Types'


class Account(models.Model):
    customer_id = models.ForeignKey(Customer, related_name='pk', on_delete=models.SET_NULL, blank=True, null=True)
    customer_name = models.ForeignKey(Customer, related_name='customer_name', on_delete=models.SET_NULL, blank=True,
                                      null=True)

    account_number = models.CharField(max_length=15)
    type = models.ForeignKey(AccountType, related_name='type', on_delete=models.SET_NULL, null=True)

    created_by = models.ForeignKey(User, related_name='created_by', on_delete=models.SET_NULL, null=True)
    create_date = models.DateTimeField(default=timezone.now)
    authorised_by = models.ForeignKey(User, related_name='authorised_by', on_delete=models.SET_NULL, null=True)
    authorise_date = models.DateTimeField()
    approved = models.BooleanField(default=False)

    def __str__(self):
        return "{} - {}".format(self.account_number, self.customer_name.__repr__())

    class Meta:
        ordering = ['customer_id']
        verbose_name_plural = 'accounts'
