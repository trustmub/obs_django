from django.utils import timezone
from django.db import models


# Create your models here.


class Country(models.Model):
    """
    This table contains all the countries that are supported in the system
    and its takes in the name of the country and the country code
    """
    name = models.CharField(max_length=100)
    country_code = models.CharField(max_length=8, default='ZAR')
    create_date = models.DateField('creation date')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'countries'


class Identification(models.Model):
    """
    This is a table containing acceptable identification document types with the following as standard
    - National ID
    - Passport Number
    """
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    create_date = models.DateField('creation date')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'identifications'


class Customer(models.Model):
    """
    this is the customer record for the client. it has foreign keys of nationality and country
    on the nationality and the country field of the address respectively.
    """
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200, null=True, blank=True)
    surname = models.CharField(max_length=200)
    dob = models.DateField('date of birth')
    id_type = models.ForeignKey(Identification, on_delete=models.CASCADE, related_name='id_type')
    id_number = models.CharField(max_length=50)
    nationality = models.ForeignKey(Country, on_delete=models.CASCADE)
    address_1 = models.CharField(max_length=100)
    address_2 = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='country')
    signature = models.CharField(max_length=100, null=True, blank=True)  # this should be an image
    avatar = models.CharField(max_length=100, null=True, blank=True)  # this should be an image
    other_details = models.TextField(null=True, blank=True)
    create_date = models.DateField('creation date', default=timezone.now)

    def __repr__(self):
        if self.middle_name is not None:
            return "{} {} {}".format(self.first_name, self.middle_name, self.surname)
        else:
            return "{} {}".format(self.first_name, self.surname)
        # return "{} {}".format(self.first_name, self.surname)

    def __str__(self):
        return "{} {}'s details".format(self.first_name, self.surname)

    @property
    def full_name(self):
        if self.middle_name is not None:
            return "{} {} {}".format(self.first_name, self.middle_name, self.surname)
        else:
            return "{} {}".format(self.first_name, self.surname)

    class Meta:
        ordering = ['first_name']
        verbose_name_plural = 'customers'
        indexes = [
            models.Index(fields=['first_name', 'surname']),
            models.Index(fields=['id_number'], name='identity_idx'),
        ]
