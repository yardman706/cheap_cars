from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("upload-cars", views.upload_car_form, name="upload_cars"),
    path("upload-car-images/<int:car_id>/", views.upload_car_images_form, name="upload_cars_images"),
    path("admin-dashboard/cars/<int:pk>/delete/", views.delete_car, name="delete_car"),
    path("admin-dashboard/images/<int:pk>/delete/", views.delete_car_image, name="delete_car_image"),
    path("inventory/", views.inventory, name="inventory"),
    path('inventory/car-details/<int:pk>/', views.car_details, name="car_details"),
]
