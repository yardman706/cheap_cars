from django.db import models


class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.email


class ContactInquiry(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.subject}"


class Car(models.Model):
    class ConditionChoices(models.TextChoices):
        USED = "Used", "Used"
        NEW = "New", "New"

    make = models.CharField(max_length=60, blank=True)
    model = models.CharField(max_length=60, blank=True)
    year = models.PositiveIntegerField(null=True, blank=True)
    profile_img = models.ImageField(upload_to="car_pics", null=True, blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=0, null=True, blank=True)
    mileage = models.PositiveIntegerField(null=True, blank=True)
    condition = models.CharField(max_length=5, choices=ConditionChoices, default=ConditionChoices.USED)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    down_payment = models.PositiveIntegerField(null=True, blank=True, default=1000)
    financing = models.PositiveIntegerField(null=True, blank=True, default=500)
    vin_number = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["-created_at"], name="car_created_at_idx"),
            models.Index(fields=["make", "model"], name="car_make_model_idx"),
            models.Index(fields=["vin_number"], name="car_vin_number_idx"),
            models.Index(fields=["condition"], name="car_condition_idx"),
        ]

    def __str__(self) -> str:
        return f'{self.id}'


class CarImage(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="car_details_pics")
    sort_order = models.PositiveSmallIntegerField(default=0)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["sort_order", "id"]
        constraints = [
            models.UniqueConstraint(fields=["car", "sort_order"], name="uniq_car_sort_order")
        ]

    def clean(self):
        from django.core.exceptions import ValidationError

        super().clean()

        qs = CarImage.objects.filter(car=self.car)
        if self.pk:
            qs = qs.exclude(pk=self.pk)
        if qs.count() >= 30:
            raise ValidationError({"image": "Each car can have at most 30 images."})

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"Image for car_id={self.car_id} (order={self.sort_order})"

