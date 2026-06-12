from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import CarForm
from .models import Car, CarImage


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


def _admin_dashboard_context(form=None):
    return {
        "form": form or CarForm(),
        "cars": Car.objects.prefetch_related("images").all(),
    }


@staff_member_required
def upload_car_form(request):
    if request.method == "POST":
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            car = form.save()
            messages.success(
                request,
                f"Car #{car.pk} created. Add gallery images in the list below.",
            )
            return redirect("upload_cars")
        return render(request, "main/post-cars.html", _admin_dashboard_context(form))

    return render(request, "main/post-cars.html", _admin_dashboard_context())


@staff_member_required
@require_POST
def delete_car(request, pk):
    car = get_object_or_404(Car, pk=pk)
    label = f"{car.year} {car.make} {car.model}".strip() or f"Car #{car.pk}"
    car.delete()
    messages.success(request, f"Deleted {label}.")
    return redirect("upload_cars")


@staff_member_required
@require_POST
def delete_car_image(request, pk):
    image = get_object_or_404(CarImage, pk=pk)
    image.delete()
    messages.success(request, "Gallery image deleted.")
    return redirect("upload_cars")


@staff_member_required
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

        messages.success(
            request,
            f"Uploaded {len(images)} image(s) to {car.year} {car.make} {car.model}.",
        )
        return redirect("upload_cars")

    return render(request, "main/post-car-images.html", {"car": car})
