from django.db import models


# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=100)
    create_date = models.DateField('creation date')

    def __str__(self):
        return self.name


class Identification(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    create_date = models.DateField('creation date')

    def __str__(self):
        return self.name


class Customer(models.Model):
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    dob = models.DateField
    id_type = models.ForeignKey(Identification, on_delete=models.CASCADE)
    id_number = models.CharField(max_length=50)
    nationality = models.CharField(max_length=100)
    address_1 = models.CharField(max_length=100)
    address_2 = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    signature = models.CharField(max_length=100)
    avatar = models.CharField(max_length=100)
    other_details = models.TextField()
    create_date = models.DateField('creation date')

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
