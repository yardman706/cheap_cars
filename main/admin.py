from django.contrib import admin
from .models import *


class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ("email", "created_at")
    search_fields = ("email",)


class ContactInquiryAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "created_at")
    search_fields = ("name", "email", "subject", "message")
    readonly_fields = ("created_at",)


class CarAdmin(admin.ModelAdmin):
    list_display = ("id", "model", "make", "year", "price")


class CarImageAdmin(admin.ModelAdmin):
    list_display = ("car", "uploaded_at")


admin.site.register(NewsletterSubscriber, NewsletterSubscriberAdmin)
admin.site.register(ContactInquiry, ContactInquiryAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(CarImage, CarImageAdmin)