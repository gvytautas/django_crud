from django.db import models
from authentication.models import User


# Create your models here.

class VehicleModel(models.Model):
    brand = models.CharField(max_length=50, null=False, blank=False)
    model = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return f'{self.model}'


class Service(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    price = models.FloatField(null=False, blank=False)

    def __str__(self):
        return f'{self.name} ({self.price})'


class Vehicle(models.Model):
    plate_number = models.CharField(max_length=50, null=False, blank=False)
    win_number = models.CharField(max_length=50, null=False, blank=False)
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    model = models.ForeignKey(VehicleModel, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='vehicles/', null=True, blank=True)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.win_number


class Order(models.Model):
    date = models.DateField(auto_now=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.vehicle.win_number} ({self.total_price})'

    @property
    def total_price(self):
        total_price = 0
        order_detail = self.order_details.all()
        for detail in order_detail:
            total_price += detail.price * detail.quantity
        return total_price


class OrderDetail(models.Model):
    quantity = models.IntegerField(null=False, blank=False)
    order = models.ForeignKey(Order, related_name='order_details', on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.order.vehicle.model.brand}'

    @property
    def price(self):
        return self.service.price
