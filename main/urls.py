from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("upload-cars", views.upload_car_form, name="upload_cars"),
    path("upload-car-images/<int:car_id>/", views.upload_car_images_form, name="upload_cars_images"),
    path("inventory/", views.inventory, name="inventory"),
    path('inventory/car-details/<int:pk>/', views.car_details, name="car_details"),
]
