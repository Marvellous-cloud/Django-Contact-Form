from django.shortcuts import render
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

            return render(request, 'contact/success.html')

    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})


def feedback(request):
    contacts = ContactMessage.objects.all()
    return render(request, 'contact/feedback.html', {
        'contacts': contacts
    })