from django.db import models

class ContactUs(models.Model):
    email = models.CharField(max_length=255, verbose_name='email')
    name = models.CharField(max_length=255, verbose_name='name', blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Contact from {self.email}'
