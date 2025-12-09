from django.shortcuts import render, redirect
from django.contrib import messages

from contact_us.forms import ContactUsForm


def home(request):
    form = ContactUsForm()
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'successfully submitted!')
            return redirect('home:home')
        else:
            print(form.errors)
            if 'email' in form.errors:
                messages.error(request, 'Invalid email address. Please correct it.')
                return redirect('home:home')
            else:
                messages.error(request, 'Please correct the errors in the form.')
                return redirect('home:home')

    context = {
        "form": form,
    }
    return render(request, 'home/home.html', context)
