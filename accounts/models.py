from django.db import models


class Customer(models.Model):
    phone_number = models.CharField('Phone number', max_length=50, null=True)
    destination = models.CharField('Destination', max_length=250, null=True)

    def __str__(self):
        return self.phone_number

    class Meta:
        verbose_name_plural = 'Customers'
