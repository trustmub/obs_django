from django.db import models


# Create your models here.

class SystemDate(models.Model):
    date = models.DateField()
    create_date = models.DateField()

    def __str__(self):
        return "Current System date is {}".format(self.date)
