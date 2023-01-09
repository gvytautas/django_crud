from django.contrib import admin
from .models import Service, VehicleModel, Vehicle, Order, OrderDetail

# Register your models here.
admin.site.register(Service)
admin.site.register(VehicleModel)
admin.site.register(Vehicle)
admin.site.register(Order)
admin.site.register(OrderDetail)
