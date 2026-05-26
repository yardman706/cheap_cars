from django import forms
from . import models

class CarForm(forms.ModelForm):
    class Meta:
        model = models.Car
        fields = ['make', 'model', 'year', 'profile_img', 'price','mileage','condition','description', 'down_payment','financing', 'vin_number']
