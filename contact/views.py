from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm
import os


def contact(request):
    """
    Handle the contact form submission and display.

    If the request method is POST, validate the form and send an email with the
    provided contact information. On successful submission, redirect back to the 
    contact page with a success message. If the request method is GET, display 
    the empty contact form.

    Args:
    - request: The HTTP request object.

    Returns:
    - HttpResponse: The rendered contact form page or a redirect to the contact page.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            send_mail(
                f'Message from {name}',
                message,
                email,
                [os.environ.get('DEFAULT_FROM_EMAIL',
                                'ntwaricedric@gmail.com')],
            )
            messages.success(
                request, 'Your message has been sent successfully!')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})
