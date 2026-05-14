from django.shortcuts import get_object_or_404, render
from .models import Car

def home(request):
    return render(request, 'main/home.html')


def inventory(request):
    cars = Car.objects.all()
    context = {"cars": cars}
    return render(request, "main/shop.html", context)


def car_details(request, pk):
    car = get_object_or_404(Car.objects.prefetch_related("images"), pk=pk)
    context = {"car": car}
    return render(request, "main/car-details.html", context)