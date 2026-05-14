from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("inventory/", views.inventory, name="inventory"),
    path('inventory/car-details/<int:pk>/', views.car_details, name="car_details"),
]
