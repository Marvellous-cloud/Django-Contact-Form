from django.shortcuts import render

# Create your views here.
from .form import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            return render(request, 'contact/success.html')

    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})