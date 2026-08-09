from django.shortcuts import render
from django.contrib import messages
from .form import ContactForm
from .models import ContactMessage

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            ContactMessage.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )

            messages.success(request, "Your message was sent successfully!")
            return render(request, 'contact/contact.html', {'form': ContactForm()})

        else:
            messages.error(request, "Please correct the errors below.")

    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})


def feedback(request):
    contacts = ContactMessage.objects.all()
    return render(request, 'contact/feedback.html', {
        'contacts': contacts
    })