from django.forms import ModelForm
from .models import VehicleModel, Vehicle


class VehicleModelForm(ModelForm):
    class Meta:
        model = VehicleModel
        fields = '__all__'


class VehicleForm(ModelForm):
    class Meta:
        model = Vehicle
        fields = ['plate_number', 'win_number', 'image', 'model']
