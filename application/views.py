from django.shortcuts import render, redirect
from .models import Service, Order, VehicleModel
from .forms import VehicleModelForm, VehicleForm
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views import View
from django.urls import reverse_lazy


# CRUD > Create Read Update Delete


# Create your views here.

def index(request):
    return render(request, 'index.html')


def show_services(request):
    services = Service.objects.values()
    return render(request, 'show_services.html', context={'services': services})


def show_orders(request):
    orders = Order.objects.filter(vehicle__model__brand__startswith='Brand').all()
    return render(request, 'show_orders.html', context={'orders': orders})


def add_vehicle_model(request):
    if request.method == 'POST':
        form = VehicleModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record created!')
            return redirect('index')
        messages.warning(request, 'Form not valid!')
        return render(request, 'add_vehicle_model.html', context={'form': form})
    else:
        form = VehicleModelForm()
    return render(request, 'add_vehicle_model.html', context={'form': form})


def show_vehicle_models(request):
    vehicle_models = VehicleModel.objects.all()
    return render(request, 'show_vehicle_models.html', context={'vehicle_models': vehicle_models})


def update_vehicle_model(request, model_id):
    if request.method == 'POST':
        vehicle_model = VehicleModel.objects.get(id=model_id)
        form = VehicleModelForm(request.POST, instance=vehicle_model)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record updated!')
            return redirect('index')
        messages.warning(request, 'Form not valid!')
        return render(request, 'add_vehicle_model.html', context={'form': form})
    else:
        form = VehicleModelForm()
    return render(request, 'add_vehicle_model.html', context={'form': form})


def add_vehicle(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST, request.FILES)
        if form.is_valid():
            vehicle = form.save(commit=False)
            vehicle.client = request.user
            vehicle.save()
            messages.success(request, 'Record created!')
            return redirect('index')
        messages.warning(request, 'Form not valid!')
        return render(request, 'add_vehicle.html', context={'form': form})
    else:
        form = VehicleForm()
    return render(request, 'add_vehicle.html', context={'form': form})


class OrderBaseView(View):
    model = Order
    fields = ['vehicle']
    success_url = reverse_lazy('all_orders')


class OrderCreateView(OrderBaseView, CreateView):
    pass
    # def get_queryset(self):
    #    self.fields['vehicle'].queryset = Vehicle.objects.filter(client=self.request.user.id)


class OrderListView(OrderBaseView, ListView):
    pass


class OrderUpdateView(OrderBaseView, UpdateView):
    pass


class OrderDeleteView(OrderBaseView, DeleteView):
    pass
