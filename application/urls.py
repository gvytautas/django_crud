from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('show_services/', views.show_services, name='show_services'),
    path('show_orders/', views.show_orders, name='show_orders'),
    path('add_vehicle_model/', views.add_vehicle_model, name='add_vehicle_model'),
    path('add_vehicle/', views.add_vehicle, name='add_vehicle'),
    path('orders/', views.OrderListView.as_view(), name='all_orders'),
    path('add_order/', views.OrderCreateView.as_view(), name='add_order'),
    path('update_order/<int:pk>/', views.OrderUpdateView.as_view(), name='update_order'),
    path('delete_order/<int:pk>/', views.OrderDeleteView.as_view(), name='delete_order'),
    path('show_vehicle_models/', views.show_vehicle_models, name='show_vehicle_models'),
    path('update_vehicle_model/<int:model_id>/', views.update_vehicle_model, name='update_vehicle_model'),
]
