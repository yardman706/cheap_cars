from django.contrib import admin
from .models import *

class CarAdmin(admin.ModelAdmin):
    list_display = ("id", "model", "make", "year", "price")

class CarImageAdmin(admin.ModelAdmin):
    list_display = ("car", "uploaded_at")

admin.site.register(Car, CarAdmin)
admin.site.register(CarImage, CarImageAdmin)