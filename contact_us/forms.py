from django import forms
from django.core.exceptions import ValidationError
import re

from .models import ContactUs

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise ValidationError("Email is required.")
        pattern = r'^[a-zA-Z0-9]+([._%+-][a-zA-Z0-9]+)*@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'
        if not re.fullmatch(pattern, email):
            raise ValidationError("Please use an email address ending with '@example.com'.")
        
        return email

