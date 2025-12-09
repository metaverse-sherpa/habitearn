from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse

from contact_us.forms import ContactUsForm


def home(request):
    form = ContactUsForm()
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thanks for joining the waitlist!')
            request.session['waitlist_success'] = True
            return redirect(f"{reverse('home:home')}#wait")
        else:
            print(form.errors)
            if 'email' in form.errors:
                messages.error(request, 'Invalid email address. Please correct it.')
                return redirect(f"{reverse('home:home')}#wait")
            else:
                messages.error(request, 'Please correct the errors in the form.')
                return redirect(f"{reverse('home:home')}#wait")

    waitlist_success = request.session.pop('waitlist_success', False)

    context = {
        "form": form,
        "waitlist_success": waitlist_success,
    }
    return render(request, 'home/home.html', context)
