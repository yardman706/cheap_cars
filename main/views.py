from django.shortcuts import get_object_or_404, redirect, render
from .models import Car, CarImage
from .forms import CarForm
from django.contrib.auth.decorators import login_required 

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

@login_required(login_url='inventory')
def upload_car_form(request):
    if request.method == "POST":
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            car = form.save()
            return redirect("upload_cars_images", car_id=car.pk)
        else:
            context = {"form": form}
            return render(request, "main/post-cars.html", context)
        
    context = {"form": CarForm()}
    return render(request, "main/post-cars.html", context)

@login_required(login_url='inventory')
def upload_car_images_form(request, car_id):
    car = get_object_or_404(Car, pk=car_id)

    if request.method == "POST":
        images = request.FILES.getlist("images")
        next_order = car.images.count()

        for offset, image in enumerate(images):
            CarImage.objects.create(
                car=car,
                image=image,
                sort_order=next_order + offset,
            )

        return redirect("car_details", pk=car.pk)

    return render(request, "main/post-car-images.html", {"car": car})