from django import forms
from . import models


class NewsletterForm(forms.ModelForm):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Your email address",
                "aria-label": "Newsletter email",
            }
        )
    )

    class Meta:
        model = models.NewsletterSubscriber
        fields = ["email"]


class ContactInquiryForm(forms.ModelForm):
    class Meta:
        model = models.ContactInquiry
        fields = ["name", "email", "subject", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Your Name"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Your Email"}),
            "subject": forms.TextInput(attrs={"class": "form-control", "placeholder": "Subject"}),
            "message": forms.Textarea(attrs={"class": "form-control", "placeholder": "Message", "rows": 6}),
        }


class CarForm(forms.ModelForm):
    class Meta:
        model = models.Car
        fields = ['make', 'model', 'year', 'profile_img', 'price','mileage','condition','description', 'down_payment','financing', 'vin_number']
